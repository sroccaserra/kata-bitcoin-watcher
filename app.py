from flask import Flask

from domaine.courtier import Courtier
from infrastructure.services.bitcoin_api_service import BitcoinApiService
from infrastructure.services.service_registry import register_service
from infrastructure.vues.achat_vue import AchatVue

app = Flask(__name__)
bitcoin_api_service = BitcoinApiService()
courtier = Courtier(bitcoin_api_service)
register_service('COURTIER', courtier)
app.add_url_rule('/', view_func=AchatVue.as_view('achat_vue'))
