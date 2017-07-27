from unittest.mock import Mock

from domaine.j_autorise_a_acheter import JAutoriseAAcheter
from infrastructure.vues.achat_vue import AchatVue


class TestAchatVue:
    def test_j_achete_si_le_courtier_est_ok(self):
        courtier: JAutoriseAAcheter = Mock(JAutoriseAAcheter)
        courtier.est_ce_que_je_peux_acheter.return_value = False
        achat_vue = AchatVue(courtier)

        assert achat_vue.dispatch_request() == "Can I buy bitcoins ? NO"

    def test_si_le_service_bitcoin_est_accessible_et_que_le_prix_est_bon_j_achete(self):
        courtier: JAutoriseAAcheter = Mock(JAutoriseAAcheter)
        courtier.est_ce_que_je_peux_acheter.return_value = True
        achat_vue = AchatVue(courtier)

        assert achat_vue.dispatch_request() == "Can I buy bitcoins ? YES"
