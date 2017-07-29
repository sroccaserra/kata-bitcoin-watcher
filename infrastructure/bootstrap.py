from flask import g

from domaine.courtier import Courtier
from infrastructure.presentateurs.presentateur import Presentateur
from infrastructure.services.bitcoin_api_service import BitcoinApiService


def get_presentateur():
    if not hasattr(g, 'presentateur'):
        g.courtier = bootstrap_presentateur()
    return g.courtier


def bootstrap_presentateur():
    bitcoin_api_service = BitcoinApiService()
    courtier = Courtier(bitcoin_api_service)
    presentateur = Presentateur(courtier)
    return presentateur
