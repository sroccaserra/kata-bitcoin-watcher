from app import est_ce_que_je_peux_acheter


class TestAchatCasNominaux:
    def test_je_peux_acheter_a_2000_dollars(self):
        assert est_ce_que_je_peux_acheter(2000)

    def test_je_ne_peux_pas_acheter_a_3000_dollars(self):
        assert not est_ce_que_je_peux_acheter(3000)

class TestAchatLimites:
    def test_je_peux_acheter_a_2400_99_dollars(self):
        assert est_ce_que_je_peux_acheter(2400.99)

    def test_je_ne_peux_pas_acheter_a_2401_dollars(self):
        assert not est_ce_que_je_peux_acheter(2401)
