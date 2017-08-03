from domaine.je_presente_la_reponse import JePresenteLaReponse


class PresentateurHtml(JePresenteLaReponse):
    def __init__(self, courtier):
        self.courtier = courtier

    def est_ce_que_je_peux_acheter(self) -> str:
        je_peux_acheter = self.courtier.est_ce_que_je_peux_acheter()
        return "<div>Can I buy bitcoins ? " + ("YES" if je_peux_acheter else "NO") + "</div>"
