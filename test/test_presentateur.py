from unittest.mock import Mock

from domaine.courtier import Courtier
from infrastructure.api.presentateurs.presentateur_html import PresentateurHtml


class TestPresentateurHtml:
    def test_je_n_achete_pas_si_le_courtier_n_est_pas_ok(self):
        courtier = Mock(Courtier)
        courtier.est_ce_que_je_peux_acheter.return_value = False
        presentateur_html = PresentateurHtml(courtier)

        reponse = presentateur_html.est_ce_que_je_peux_acheter()

        assert reponse == "<div>Can I buy bitcoins ? NO</div>"

    def test_j_achete_si_le_courtier_est_ok(self):
        courtier = Mock(Courtier)
        courtier.est_ce_que_je_peux_acheter.return_value = True
        presentateur_html = PresentateurHtml(courtier)

        reponse = presentateur_html.est_ce_que_je_peux_acheter()

        assert reponse == "<div>Can I buy bitcoins ? YES</div>"
