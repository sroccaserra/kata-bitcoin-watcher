from flask.views import View

from domaine.j_autorise_a_acheter import JAutoriseAAcheter
from infrastructure.services.service_registry import get_service


class AchatVue(View):
    def __init__(self, courtier: JAutoriseAAcheter = None):
        if courtier is None:
            self.courtier: JAutoriseAAcheter = get_service('COURTIER')
        else:
            self.courtier: JAutoriseAAcheter = courtier

    def dispatch_request(self):
        je_peux_acheter = self.courtier.est_ce_que_je_peux_acheter()
        return "Can I buy bitcoins ? " + ("YES" if je_peux_acheter else "NO")
