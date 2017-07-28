from flask import g

from domaine.courtier import Courtier
from infrastructure.services.bitcoin_api_service import BitcoinApiService


def get_courtier():
    if not hasattr(g, 'courtier'):
        g.courtier = bootstrap_courtier()
    return g.courtier


def bootstrap_courtier():
    bitcoin_api_service = BitcoinApiService()
    courtier = Courtier(bitcoin_api_service)
    return courtier
