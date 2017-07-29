from unittest.mock import Mock

from domaine.courtier import Courtier
from domaine.j_obtiens_le_cours_du_bitcoin import JObtiensLeCoursDuBitcoin


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
        bitcoin_api_service = Mock(JObtiensLeCoursDuBitcoin)
        bitcoin_api_service.recupere_le_cours_actuel_du_bitcoin.side_effect = \
            Exception()
        courtier = Courtier(bitcoin_api_service)

        assert not courtier.est_ce_que_je_peux_acheter()


def _build_courtier(cours_du_bitcoin):
    bitcoin_api_service = Mock(JObtiensLeCoursDuBitcoin)
    bitcoin_api_service.recupere_le_cours_actuel_du_bitcoin.return_value = cours_du_bitcoin

    return Courtier(bitcoin_api_service)
