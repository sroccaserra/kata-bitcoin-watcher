from domaine.je_presente_la_reponse import JePresenteLaReponse


class Presentateur(JePresenteLaReponse):
    def __init__(self, courtier):
        self.courtier = courtier

    def est_ce_que_je_peux_acheter(self):
        je_peux_acheter = self.courtier.est_ce_que_je_peux_acheter()
        return "Can I buy bitcoins ? " + ("YES" if je_peux_acheter else "NO")
