from flask import Flask, jsonify, request, Blueprint
from utils.functions import open_db, get_aluno

app = Flask(__name__)

saudacao_bp = Blueprint("saudacao", __name__)

@saudacao_bp.route('/saudacao')
def saudacao():
    aluno_req = request.args.get('aluno')
    if not aluno_req:
        return jsonify(error='Please provide a student name.'), 400

    db = open_db()
    
    aluno = get_aluno(aluno_req, db)
    if not aluno:
        return jsonify(error='Student not found or name malformed.'), 404
    
    return jsonify(data=f"Olá, {aluno.get('name')}.")
    