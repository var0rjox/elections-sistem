from flask import Blueprint, request


vote = Blueprint('vote', __name__, url_prefix="/send_vote")

@vote.route('/', methods = ['GET', 'POST'])
def voter():
     return 'Voto procesado' if request.method == 'POST' else 'Esta es la seccion para votar'