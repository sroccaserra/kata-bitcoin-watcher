from typing import Dict, Any

from domaine.je_presente_la_reponse import JePresenteLaReponse


class PresentateurDict(JePresenteLaReponse):
    def __init__(self, courtier):
        self.courtier = courtier

    def est_ce_que_je_peux_acheter(self) -> Dict[str, Any]:
        je_peux_acheter = self.courtier.est_ce_que_je_peux_acheter()
        return {'can_I_buy_bitcoins': je_peux_acheter}
