from flask import Flask, jsonify, request, Blueprint
from utils.helpers import validate_and_get_aluno

app = Flask(__name__)

saudacao_bp = Blueprint("saudacao", __name__)

@saudacao_bp.route('/saudacao')
def saudacao():
    aluno, error = validate_and_get_aluno(request.args)
    if error:
        return error

    return jsonify(data=f"Olá, {aluno.get('name')}.")
    