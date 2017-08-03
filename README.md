# Kata Bitcoin Watcher

Comment organiser du code pour qu'il soit testable / changeable / nettoyable ?

Kata sur ce thème à l'aide d'une minuscule application Web.


## Objectif de la minuscule application

Savoir si acheter des bitcoins est "intéressant", grâce à un "site Web" (l'application), en s'appuyant sur un service externe (l'[API Bitcoin](https://api.blockchain.info/stats)).


## Code de départ

```python
# Fichier : app.py

import requests
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    response = requests.get('https://api.blockchain.info/stats')
    market_price_usd = response.json()['market_price_usd']
    can_i_buy = market_price_usd < 2596.22
    return "Can I buy bitcoins ? " + ("YES" if can_i_buy else "NO")
```

Si l'application reste minuscule (~= 10 lignes de code), ce premier jet n'est pas un problème.

Mais dès que l'application va grossir (au bout de quelques jours), cette approche va poser de plus en plus de problèmes car toutes les intentions sont mélangées :

- L'appel à l'API blockchain (service externe),
- La déserialisation du message fournit par le service externe,
- La règle métier qui décide ou non si on doit acheter,
- Le formatage du message retourné à l'utilisateur,
- La configuration du framework Web.

Si on continue dans cette voie, ces notions vont rester mélangées à travers l'application. Et on aura de plus en plus de mal à les comprendre et les faire évoluer. Et les notions métier seront éclipsées par les aspects techs.


## Objectif du kata

Réfléchir sur comment on peut tester / implémenter / modifier ces intentions indépendamment les unes des autres, et pour ça comment on les organiserait autrement.

Par exemple, comment tester une règle métier indépendamment du reste du programme, comment tester un service externe indépendamment du reste du programme...

Peut-on tester toutes les règles métier avec des tests unitaires ?

Et peut-on avoir un test d'acceptance indépendant du framework Web et du service externe ?

Autrement dit, comment on peut avoir une architecture facilement testable ?

Et une architecture testable permet de changer le code plus facilement, et du code plus facile à changer permet de maintenir du code propre plus facilement.

## Implémentation proposée en exemple

Dans l'implémentation proposée dans ce dépôt Git, j'ai utilisé les principes de l'architecture hexagonale, qui est un exemple d'architecture testable, pour répondre aux objectifs du kata.

Cette architecture logicielle a les avantages :
- d'avoir une forme de base simple (trois couches seulement),
- de rendre les couches faciles à tester isolément,
- et de pouvoir conserver sa simplicité quand la base de code grossit : les principes qu'on voit sur cette mini application s'appliquent quasi tel quel sur des applications bien plus grosses.


### API || Domaine || Services extérieurs

En résumé vite fait :
1. La mini application est découpée en trois partie distinctes :
    - Ce que fournit le programme aux utilisateurs, une API
    - Le domaine, ce que fait le programme en interne au sens purement métier
    - Les services extérieurs dont a besoin le programme (les données sur le cours du bitcoin)
2. Et le domaine ne dépend absolument pas du reste.

**Domaine**

Dans le répertoire `domaine`, il y a toutes les règles métiers (dans l'exemple, deux) qui permettent de décider si on peut acheter ou non des bitcoins.

Tout le code du répertoire `domaine` ne dépend ni du code de l'API fournie, ni du code appelant les services extérieurs. C'est une règle importante, qui permet de tester entièrement les règles métier unitairement, indépendamment du framework Web et de tous les services externes (voir [test_courtier.py](test/test_courtier.py)).

Le domaine ne dépend pas du reste du code pour se définir, c'est le reste du code qui dépend du domaine pour se définir. Mais il a besoin de communiquer avec le reste du code. Pour ça, dans ce petit exemple, le domaine définit deux interfaces (ce sont les ports de l'architecture hexagonale).
- Une interface pour interroger le domaine ([JePresenteLaReponse](domaine/je_presente_la_reponse.py)) que va utiliser l'API que fournit le programme.
- Une interface que le service externe va implémenter ([JObtiensLeCoursDuBitcoin](domaine/j_obtiens_le_cours_du_bitcoin.py)) pour pouvoir être injecté dans le domaine.

**Infrastructure**

Dans le répertoire infrastructure, on trouve le code :
- de l'API que fournit le programme (répertoire `infrastructure/api`),
- des services extérieurs dont a besoin le programme (répertoire `infrastructure/services`).

Le répertoire `infrastructure/api` contient deux choses.

- Un adaptateur ([Presentateur](infrastructure/api/presentateurs/presentateur_html.py)), dans lequel on injecte une classe métier. Le rôle de cet adaptateur et de présenter les données fournies par le métier sous une forme exploitable par le controlleur Web. Ce présentateur est testable indépendamment du framework Web (ici Flask).
- Un controlleur Web, qui utilise le framework Web et le présentateur pour fournir la fonctionnalité à l'utilisateur final.

Le répertoire `infrastructure/services` contient aussi un adaptateur, qui implémente le port `JObtiensLeCoursDuBitcoin` définit par le domaine. Cet adaptateur requête le service externe, et formate correctement la réponse pour la renvoyer au domaine.


### Bootstrap

Comment on bootstrap tout ça ?

On a vu que pour la définition des classes, le controlleur et son présentateur dépendent du domaine, et l'adaptateur vers le service extérieur dépend aussi du domaine (car il implémente le port définit dans le domaine).

Mais pour l'instantiation de ces classes, les différentes injection de dépendances sont dans ce sens : on injecte une instance du service externe dans une instance du domaine. et ensuite, on injecte l'instance du domaine dans le présentateur dont dépend le controlleur.

Pour résumer, les dépendances (`A -> B` : `A` a besoin d'une définition de `B` pour se définir) sont comme ça :

`controlleur -> présentateur -> domaine <- service`

Et l'injection de dépendances (`A -> B` : `A` a besoin d'une instance de `B` pour s'instancier) est comme ça :

`controlleur -> présentateur -> domaine -> service`

Donc pour le bootstrap, on instancie d'abord le service, puis le domaine, puis le présentateur et le controlleur (voir [bootstrap.py](infrastructure/bootstrap.py)). 

Ce bootstrap se retrouve dans le test d'acceptance ([test_acceptance.py](test/test_acceptance.py)), où on mock le service et on fait l'économie de la route HTTP, mais où tout le reste est instancié et bootstrapé normalement (c'est quasi un test complet, mais qui reste unitaire quand le setup est simple).


## Tech

Testé avec Python 3.6.2, et voir le `Makefile` pour plus d'infos.


## Voir aussi

Fortement inspiré / copié de :

- <https://github.com/celinegilet/blockchain-api>

Sur l'architecture, voir aussi :

- [L'Après-midi du DDD](https://gist.github.com/sroccaserra/8681ea5fadc6a1dfb3bbeb0e4f6fe395)
- [Alistair in the 'hexagone'](https://gist.github.com/sroccaserra/d37aa6538696b5d94369ab13fbe3e63b)
- [Robert C Martin - Clean Architecture and Design (vidéo)](https://www.youtube.com/watch?v=Nsjsiz2A9mg)

Kata faisable dans le même esprit, un poil plus compliqué :

- [Kata Train Reservation](https://github.com/sroccaserra/kata-train-reservation)
