from flask.views import View

from infrastructure.bootstrap import get_presentateur


class AchatVue(View):
    def __init__(self, presentateur=None):
        self.presentateur = presentateur or get_presentateur()

    def dispatch_request(self):
        return self.presentateur.est_ce_que_je_peux_acheter()
