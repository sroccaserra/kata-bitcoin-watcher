from flask import Flask

from infrastructure.api.vues.achat import achat

app = Flask(__name__)
app.register_blueprint(achat)
