from unittest.mock import patch

from app import hello


@patch("app.recupere_le_cours_actuel_du_bitcoin")
def test_si_le_service_bitcoin_n_est_pas_accessible_je_n_achete_pas(recupere_le_cours_actuel_du_bitcoin):
    recupere_le_cours_actuel_du_bitcoin.side_effect = Exception()
    assert hello() == "Can I buy bitcoins ? NO"
