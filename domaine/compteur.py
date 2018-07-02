class Compteur:
    def __init__(self):
        self._valeur = 0

    def valeur(self):
        return self._valeur

    def incremente(self):
        self._valeur += 1
