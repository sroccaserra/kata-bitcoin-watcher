from domaine.j_obtiens_le_cours_du_bitcoin import JObtiensLeCoursDuBitcoin


class Courtier:
    def __init__(self, bitcoin_api_service: JObtiensLeCoursDuBitcoin):
        self.bitcoin_api_service = bitcoin_api_service

    def est_ce_que_je_peux_acheter(self) -> bool:
        try:
            cours_du_bitcoin = self.bitcoin_api_service.recupere_le_cours_actuel_du_bitcoin()
        except:
            return False
        else:
            return cours_du_bitcoin < 2401
