# Kata Bitcoin Watcher

Comment organiser du code pour qu'il soit testable / changeable / nettoyable ?

Kata sur ce thème à l'aide d'une minuscule application Web.


## Objectif de la minuscule application

Savoir si acheter des bitcoins est "intéressant", grâce à une API HTTP (notre application), en s'appuyant sur un service externe (l'[API Bitcoin](https://api.blockchain.info/stats)).


## Code de départ

```python
# Fichier : app.py

import requests
from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/")
def home():
    response = requests.get('https://api.blockchain.info/stats')
    market_price_usd = response.json()['market_price_usd']
    can_i_buy = market_price_usd < 2596.22
    return jsonify({'can_I_buy_bitcoins': can_i_buy})
```

Si notre application reste minuscule (~= 10 lignes de code), ce premier jet n'est pas un problème.

Mais dès que notre application va grossir (au bout de quelques jours), cette approche va poser de plus en plus de problèmes car toutes les intentions sont mélangées :

- L'appel à l'API blockchain (service externe),
- La déserialisation du message fournit par le service externe,
- La règle métier qui décide ou non si on doit acheter,
- Le formatage du message retourné à l'utilisateur,
- La configuration du framework Web.

Si on continue dans cette voie, ces notions vont rester mélangées à travers notre application. Et on aura de plus en plus de mal à les comprendre et les faire évoluer. Et les notions métier seront éclipsées par les aspects techs.


## Objectif du kata

Réfléchir sur comment on peut tester / implémenter / modifier ces intentions indépendamment les unes des autres, et pour ça comment on les organiserait autrement.

Par exemple, comment tester une règle métier indépendamment du reste du programme, comment tester un service externe indépendamment du reste du programme...

Peut-on tester toutes les règles métier avec des tests unitaires ?

Et peut-on avoir un test d'acceptance indépendant du framework Web et du service externe ?

Autrement dit, comment on peut avoir une architecture facilement testable ?

Note : pourquoi avoir une architecture testable ? Car une architecture testable permet de changer le code plus facilement, et du code plus facile à changer permet de maintenir du code propre plus facilement.


## Implémentation proposée en exemple

Dans l'implémentation proposée dans ce dépôt Git, j'ai utilisé les principes de l'architecture hexagonale, qui est un exemple d'architecture testable, pour répondre aux objectifs du kata.

Cette architecture logicielle a les avantages :
- d'avoir une forme de base simple (trois couches seulement),
- de rendre les couches faciles à tester isolément,
- et de pouvoir conserver sa simplicité quand la base de code grossit : les principes qu'on voit sur cette minuscule application s'appliquent quasi tel quel sur des applications bien plus grosses.


### API || Domaine || Services externes

En résumé vite fait, on a deux règles strictes :
1. Notre application est découpée en trois partie distinctes :
    - Ce que fournit le programme aux utilisateurs (une API)
    - Le domaine, ce que fait le programme en interne au sens purement métier (décider si on peut acheter ou non)
    - Les services externes dont a besoin le programme (les données sur le cours du bitcoin)
2. Le code du domaine ne dépend absolument pas du reste.

### Domaine

Dans le répertoire `domaine`, il y a toutes les règles métiers (dans l'exemple, deux) qui permettent de décider si on peut acheter ou non des bitcoins.

Tout le code du répertoire `domaine` ne dépend ni du code de l'API fournie, ni du code appelant les services externes. C'est une règle importante, qui permet de tester entièrement les règles métier unitairement, indépendamment du framework Web et de tous les services externes (voir [test_courtier.py](test/test_courtier.py)).

Le domaine ne dépend pas du reste du code pour se définir, c'est le reste du code qui dépend du domaine pour se définir. Mais il a besoin de communiquer avec le reste du code. Pour ça, dans ce petit exemple, le domaine définit deux interfaces (ce sont les ports de l'architecture hexagonale).
- Une interface pour interroger le domaine ([JePresenteLaReponse](domaine/je_presente_la_reponse.py)) que va utiliser l'API que fournit le programme.
- Une interface que le service externe va implémenter ([JObtiensLeCoursDuBitcoin](domaine/j_obtiens_le_cours_du_bitcoin.py)) pour pouvoir être injecté dans le domaine.

### Infrastructure

Dans le répertoire infrastructure, on trouve :
- l'API que fournit le programme (répertoire `infrastructure/application`),
- les services externes dont a besoin le programme (répertoire `infrastructure/services_externes`).

#### Application

Le répertoire `infrastructure/application` contient deux choses.

- Notre application qui utilise le framework Web (Flask) et présente la fonctionnalité à l'utilisateur final,
- Un adaptateur ([PresentateurDict](infrastructure/application/presentateurs/presentateur_dict.py)), dans lequel on injecte une classe métier. Le rôle de cet adaptateur et de présenter les données fournies par le métier sous une forme exploitable par notre application Web (ici un `dict` facile à transformer en JSON). Ce présentateur est testable indépendamment du framework Web choisi par l'application (ici Flask).

#### Services externes

Le répertoire `infrastructure/services_externes` contient aussi un adaptateur, qui implémente le port `JObtiensLeCoursDuBitcoin` définit par le domaine. Cet adaptateur requête le service externe, et formate correctement la réponse pour la renvoyer au domaine.


### Bootstrap

Comment on bootstrap tout ça ?

On a vu que pour la définition des classes, la Web app et son présentateur dépendent du domaine, et l'adaptateur vers le service extérieur dépend aussi du domaine (car il implémente le port définit dans le domaine).

Mais pour l'instantiation de ces classes, les différentes injection de dépendances sont dans ce sens : on injecte une instance du service externe dans une instance du domaine. Et ensuite, on injecte l'instance du domaine dans le présentateur dont dépend notre application Web.

Pour résumer, les dépendances (`A -> B` : `A` a besoin d'une définition de `B` pour se définir) sont comme ça :

`présentateur -> domaine <- service`

Et l'injection de dépendances (`A -> B` : `A` a besoin d'une instance de `B` pour s'instancier) est comme ça :

`présentateur -> domaine -> service`

Donc pour le bootstrap, on instancie d'abord le service, puis le domaine, puis le présentateur (voir [bootstrap.py](infrastructure/bootstrap.py)). 

Ce bootstrap se retrouve dans le test d'acceptance ([test_acceptance.py](test/test_acceptance.py)), où on mock le service et on fait l'économie de la route HTTP, mais où tout le reste est instancié et bootstrapé normalement. C'est quasi un test complet, mais qui reste unitaire quand le setup est simple.


## Tech

Testé avec Python 3.6.2, et voir le `Makefile` pour plus d'infos.


## Voir aussi

Fortement inspiré / copié de :

- <https://github.com/celinegilet/blockchain-api>

Sur l'architecture, voir aussi :

- [Hexagonal architecture (l'article original)](http://alistair.cockburn.us/Hexagonal+architecture)
- [A Little Architecture - Robert C Martin](http://blog.cleancoder.com/uncle-bob/2016/01/04/ALittleArchitecture.html)
- [L'Après-midi du DDD](https://gist.github.com/sroccaserra/8681ea5fadc6a1dfb3bbeb0e4f6fe395)
- [Alistair in the 'hexagone'](https://gist.github.com/sroccaserra/d37aa6538696b5d94369ab13fbe3e63b)
- [Clean Architecture and Design - Robert C Martin (vidéo)](https://www.youtube.com/watch?v=Nsjsiz2A9mg)

Kata faisable dans le même esprit, un poil plus compliqué :

- [Kata Train Reservation](https://github.com/sroccaserra/kata-train-reservation)

## Feedback n° 1

- Comment on justifie la valeur des test, de ce découpage ?
- Préciser : on ne fait pas 20 couches mais seulement 3
- Objectif de faire ça ?
- C'est quoi la limite ?
- Dessin linéaire => faire plutôt circulaire ?
- Appuyer plus sur la mise en valeur du métier
- Exemple métier trop simple ?
- Bien préciser que ça scale
- Indiquer "qu'est-ce qui va où" et pourquoi ?
- Aller plus lentement quand on lit ligne par ligne
- Challenger l'ordre, commencer par les parties les plus évidentes
- Utiliser les questions qu'on se pose en le codant, raconter son raisonnement pour expliquer le pourquoi.
- Des parties du code plus importantes que d'autres
- Autre idée : comment ajouter une nouvelle fonctionnalité, par exemple : "j'achète du bitcoin si c'est moins cher que les dix derniers prix" Alors il faut un historique, comment la structure le permet super facilement, en sachant où on range les choses par oposition au code de départ, où on ne saurait pas où mettre les choses.
