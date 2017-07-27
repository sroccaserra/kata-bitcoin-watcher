from unittest.mock import Mock

from domaine.courtier import Courtier
from domaine.j_obtiens_le_cours_du_bitcoin import JObtiensLeCoursDuBitcoin
from infrastructure.vues.achat_vue import AchatVue


class TestAcceptance:
    def test_j_achete_si_le_cours_du_bitcoin_est_bon(self):
        bitcoin_api_service:JObtiensLeCoursDuBitcoin = Mock(JObtiensLeCoursDuBitcoin)
        bitcoin_api_service.recupere_le_cours_actuel_du_bitcoin.return_value = 2000
        courtier = Courtier(bitcoin_api_service)
        achat_vue = AchatVue(courtier)

        vue = achat_vue.dispatch_request()

        assert vue == "Can I buy bitcoins ? YES"
