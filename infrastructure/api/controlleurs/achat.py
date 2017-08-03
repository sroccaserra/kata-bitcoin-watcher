from flask import Blueprint, jsonify

from infrastructure.bootstrap import get_presentateur

achat = Blueprint('achat', __name__)


@achat.route('/')
def home():
    reponse_formatee = get_presentateur().est_ce_que_je_peux_acheter()
    return jsonify(reponse_formatee)
