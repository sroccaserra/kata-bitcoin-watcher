from domaine.compteur import Compteur


class TestCompteur:
    def test_initialisation_compteur(self):
        compteur = Compteur()
        assert compteur.valeur() == 0

    def test_incrementation_compteur(self):
        compteur = Compteur()
        compteur.incremente()
        assert compteur.valeur() == 1
