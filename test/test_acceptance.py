from domaine.courtier import Courtier
from infrastructure.application.presentateurs.presentateur_dict import PresentateurDict
from test.bitcoin_api_fake_service import BitcoinApiFakeService


class TestAcceptance:
    def test_j_achete_si_le_cours_du_bitcoin_est_bon(self):
        bitcoin_api_service = BitcoinApiFakeService(2000)
        courtier = Courtier(bitcoin_api_service)
        presentateur = PresentateurDict(courtier)

        reponse = presentateur.est_ce_que_je_peux_acheter()

        assert reponse == {'can_I_buy_bitcoins': True}
