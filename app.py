from flask import Flask

from infrastructure.vues.achat_vue import AchatVue

app = Flask(__name__)
app.add_url_rule('/', view_func=AchatVue.as_view('achat_vue'))
