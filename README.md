## Objectif de l'application

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

Si l'application reste aussi petite, ce code n'est pas forcément un problème.

Mais dès que l'application va grossir (au bout de quelques jours), cette approche va poser de plus en plus de problèmes car toutes les intentions sont mélangées :

- L'appel à l'API blockchain (service externe),
- La déserialisation du message fournit par le service externe,
- La règle métier qui décide ou non si on doit acheter,
- Le formatage du message retourné à l'utilisateur.

Si on continue dans cette voie, toutes ces notions vont rester mélangées à travers l'application. Et on aura de plus en plus de mal à les comprendre et les faire évoluer. Et les notions métier seront eclipsées par les aspects techs.


## Objectif du kata

Réfléchir sur comment on peut tester / implémenter ces intentions, et pour ça comment on les organiserait autrement. Par exemple, comment tester une règle métier indépendamment du reste du programme, comment tester un service externe indépendamment du reste du programme...


## Tech

Testé avec Python 3.6.2, et voir le `Makefile` pour plus d'infos.


## Voir aussi

Inspiré de :

- <https://github.com/celinegilet/blockchain-api>
