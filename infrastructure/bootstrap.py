from flask import g

from domaine.courtier import Courtier
from infrastructure.application.presentateurs.presentateur_dict import PresentateurDict
from infrastructure.services_externes.bitcoin_api_http_service import BitcoinApiHttpService


def get_presentateur():
    if not hasattr(g, 'presentateur'):
        g.courtier = bootstrap_presentateur()
    return g.courtier


def bootstrap_presentateur():
    bitcoin_api_service = BitcoinApiHttpService()
    courtier = Courtier(bitcoin_api_service)
    return PresentateurDict(courtier)
