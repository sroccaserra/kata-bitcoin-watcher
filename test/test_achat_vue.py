from unittest.mock import Mock

from domaine.j_autorise_a_acheter import JAutoriseAAcheter
from infrastructure.vues.achat_vue import AchatVue


class TestAchatVue:
    def test_je_n_achete_pas_si_le_courtier_n_est_pas_ok(self):
        courtier: JAutoriseAAcheter = Mock(JAutoriseAAcheter)
        courtier.est_ce_que_je_peux_acheter.return_value = False
        achat_vue = AchatVue(courtier)

        vue = achat_vue.dispatch_request()

        assert vue == "Can I buy bitcoins ? NO"

    def test_j_achete_si_le_courtier_est_ok(self):
        courtier: JAutoriseAAcheter = Mock(JAutoriseAAcheter)
        courtier.est_ce_que_je_peux_acheter.return_value = True
        achat_vue = AchatVue(courtier)

        vue = achat_vue.dispatch_request()

        assert vue == "Can I buy bitcoins ? YES"
