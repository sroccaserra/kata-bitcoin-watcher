from domaine.courtier import Courtier
from test.bitcoin_api_fake_service import BitcoinApiFakeService
from test.bitcoin_api_unavailable_service import \
    BitcoinApiUnavailableService


class TestAchatCasNominaux:
    def test_je_peux_acheter_a_2000_dollars(self):
        courtier = _build_courtier(2000)
        assert courtier.est_ce_que_je_peux_acheter()

    def test_je_ne_peux_pas_acheter_a_3000_dollars(self):
        courtier = _build_courtier(3000)
        assert not courtier.est_ce_que_je_peux_acheter()


class TestAchatLimites:
    def test_je_peux_acheter_a_2400_99_dollars(self):
        courtier = _build_courtier(2400.99)
        assert courtier.est_ce_que_je_peux_acheter()

    def test_je_ne_peux_pas_acheter_a_2401_dollars(self):
        courtier = _build_courtier(2401)
        assert not courtier.est_ce_que_je_peux_acheter()


class TestIndisponibiliteDuServiceBitcoin:
    def test_si_le_service_bitcoin_n_est_pas_accessible_je_n_achete_pas(self):
        bitcoin_api_service = BitcoinApiUnavailableService()
        courtier = Courtier(bitcoin_api_service)

        assert not courtier.est_ce_que_je_peux_acheter()


def _build_courtier(cours_du_bitcoin):
    bitcoin_api_service = BitcoinApiFakeService(cours_du_bitcoin)
    return Courtier(bitcoin_api_service)
