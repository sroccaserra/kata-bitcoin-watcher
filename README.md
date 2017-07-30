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

Si on continue dans cette voie, ces notions vont rester mélangées à travers l'application. Et on aura de plus en plus de mal à les comprendre et les faire évoluer. Et les notions métier seront eclipsées par les aspects techs.


## Objectif du kata

Réfléchir sur comment on peut tester / implémenter / modifier ces intentions indépendamment les unes des autres, et pour ça comment on les organiserait autrement.

Par exemple, comment tester une règle métier indépendamment du reste du programme, comment tester un service externe indépendamment du reste du programme...

Peut-on tester toutes les règles métier avec des tests unitaires ?

Et peut-on avoir un test d'acceptance indépendant du framework Web et du service externe ?

Autrement dit, comment on peut avoir une architecture facilement testable ?

Et une architecture testable permet de changer le code plus facilement, et du code plus facile à changer permet de maintenir du code propre plus facilement.


## Tech

Testé avec Python 3.6.2, et voir le `Makefile` pour plus d'infos.


## Voir aussi

Fortement inspiré / copié de :

- <https://github.com/celinegilet/blockchain-api>

Sur l'architecture, voir aussi :

- [L'Après-midi du DDD](https://gist.github.com/sroccaserra/8681ea5fadc6a1dfb3bbeb0e4f6fe395)
- [Alistair in the 'hexagone'](https://gist.github.com/sroccaserra/d37aa6538696b5d94369ab13fbe3e63b)

Kata dans le même esprit, un poil plus compliqué :

- [Kata Train Reservation](https://github.com/sroccaserra/kata-train-reservation)
