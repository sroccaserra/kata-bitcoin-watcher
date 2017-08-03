from unittest.mock import Mock

from domaine.courtier import Courtier
from domaine.j_obtiens_le_cours_du_bitcoin import JObtiensLeCoursDuBitcoin
from infrastructure.application.presentateurs.presentateur_dict import PresentateurDict


class TestAcceptance:
    def test_j_achete_si_le_cours_du_bitcoin_est_bon(self):
        bitcoin_api_service = Mock(JObtiensLeCoursDuBitcoin)
        bitcoin_api_service.recupere_le_cours_actuel_du_bitcoin.return_value = 2000
        courtier = Courtier(bitcoin_api_service)
        presentateur = PresentateurDict(courtier)

        reponse = presentateur.est_ce_que_je_peux_acheter()

        assert reponse == {'can_I_buy_bitcoins': True}
