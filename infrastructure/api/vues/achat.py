from flask import Blueprint

from infrastructure.bootstrap import get_presentateur

achat = Blueprint('achat', __name__)


@achat.route('/')
def home():
    return get_presentateur().est_ce_que_je_peux_acheter()
