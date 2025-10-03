from flask import Flask, jsonify, request, Blueprint
from utils.helpers import validate_and_get_aluno

app = Flask(__name__)

curso_bp = Blueprint("curso", __name__)

@curso_bp.route('/curso')
def curso():
    aluno, error = validate_and_get_aluno(request.args)
    if error:
        return error

    # Get student's course
    curso = aluno.get('curso')
    if not curso:
        return jsonify(error='Student does not have a registered course.'), 400
    
    return jsonify(data=curso)
    