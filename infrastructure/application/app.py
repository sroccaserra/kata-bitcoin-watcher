from flask import Flask, jsonify

from infrastructure.bootstrap import get_presentateur

app = Flask(__name__)


@app.route('/')
def home():
    reponse_formatee = get_presentateur().est_ce_que_je_peux_acheter()
    return jsonify(reponse_formatee)
