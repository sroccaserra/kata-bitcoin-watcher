from flask.views import View

from infrastructure.services.service_registry import get_service


class AchatVue(View):
    def __init__(self, courtier=None):
        self.courtier = courtier or get_service('COURTIER')

    def dispatch_request(self):
        je_peux_acheter = self.courtier.est_ce_que_je_peux_acheter()
        return "Can I buy bitcoins ? " + ("YES" if je_peux_acheter else "NO")
