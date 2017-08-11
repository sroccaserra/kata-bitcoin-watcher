## Domaine

Dans le répertoire `domaine`, il y a toutes les règles métiers (dans l'exemple, deux) qui permettent de décider si on peut acheter ou non des bitcoins.

Règle d'or : tout le code du répertoire `domaine` ne dépend absolument pas du reste du code (ni du code de l'API fournie, ni du code appelant les services externes) pour se définir. Aucun `import` de l'infrastructure dans ce répertoire. 

C'est une règle importante, qui permet de réfléchir au métier indépendamment de tout le reste (réseau, base de données, l'infrastructure au sens large).

Ça perment aussi  de tester entièrement les règles métier indépendamment du framework Web et de tous les services externes (voir [test_courtier.py](../test/test_courtier.py)).
