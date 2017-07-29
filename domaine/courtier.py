from domaine.je_presente_la_reponse import JePresenteLaReponse


class Courtier(JePresenteLaReponse):
    def __init__(self, bitcoin_api_service):
        self.bitcoin_api_service = bitcoin_api_service

    def est_ce_que_je_peux_acheter(self) -> bool:
        try:
            cours_du_bitcoin = self.bitcoin_api_service.recupere_le_cours_actuel_du_bitcoin()
        except:
            return False
        else:
            return cours_du_bitcoin < 2401
