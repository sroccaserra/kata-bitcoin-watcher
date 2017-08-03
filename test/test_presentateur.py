from unittest.mock import Mock

from domaine.courtier import Courtier
from infrastructure.api.presentateurs.presentateur_dict import PresentateurDict


class TestPresentateurHtml:
    def test_je_n_achete_pas_si_le_courtier_n_est_pas_ok(self):
        courtier = Mock(Courtier)
        courtier.est_ce_que_je_peux_acheter.return_value = False
        presentateur_html = PresentateurDict(courtier)

        reponse = presentateur_html.est_ce_que_je_peux_acheter()

        assert reponse == {'can_I_buy_bitcoins': False}

    def test_j_achete_si_le_courtier_est_ok(self):
        courtier = Mock(Courtier)
        courtier.est_ce_que_je_peux_acheter.return_value = True
        presentateur_html = PresentateurDict(courtier)

        reponse = presentateur_html.est_ce_que_je_peux_acheter()

        assert reponse == {'can_I_buy_bitcoins': True}
