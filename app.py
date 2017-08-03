from flask import Flask

from infrastructure.api.controlleurs.achat import achat

app = Flask(__name__)
app.register_blueprint(achat)
