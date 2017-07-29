from unittest import TestCase
from unittest.mock import Mock

from domaine.courtier import Courtier
from infrastructure.presentateurs.presentateur import Presentateur


class TestPresentateur(TestCase):
    def test_je_n_achete_pas_si_le_courtier_n_est_pas_ok(self):
        courtier = Mock(Courtier)
        courtier.est_ce_que_je_peux_acheter.return_value = False
        presentateur = Presentateur(courtier)

        reponse = presentateur.est_ce_que_je_peux_acheter()

        assert reponse == "Can I buy bitcoins ? NO"

    def test_j_achete_si_le_courtier_est_ok(self):
        courtier = Mock(Courtier)
        courtier.est_ce_que_je_peux_acheter.return_value = True
        presentateur = Presentateur(courtier)

        reponse = presentateur.est_ce_que_je_peux_acheter()

        assert reponse == "Can I buy bitcoins ? YES"
