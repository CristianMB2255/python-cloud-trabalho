from flask import jsonify
from utils.functions import open_db, get_aluno

def validate_and_get_aluno(args):
    aluno_req = args.get('aluno')
    if not aluno_req:
        return None, (jsonify(error='Please provide a student name.'), 400)

    db = open_db()
    if not db:
        jsonify(error='Error trying to open file.'), 500

    aluno = get_aluno(aluno_req, db)
    if not aluno:
        return None, (jsonify(error='Student not found or name malformed.'), 404)
    
    return aluno, None