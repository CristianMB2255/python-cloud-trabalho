from flask import Flask, jsonify, request, Blueprint
from utils import open_db, get_aluno

app = Flask(__name__)

curso_bp = Blueprint("curso", __name__)

@curso_bp.route('/curso')
def curso():
    aluno_req = request.args.get('aluno')
    if not aluno_req:
        return jsonify(error='Please provide a student name.'), 400

    db = open_db()
    
    aluno = get_aluno(aluno_req, db)
    if not aluno:
        return jsonify(error='Student not found or name malformed.'), 404

    # Get student's course
    curso = aluno.get('curso')
    if not curso:
        return jsonify(error='Student does not have a registered course.'), 400
    
    return jsonify(data=curso)
    