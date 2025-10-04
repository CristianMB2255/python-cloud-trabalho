from flask import Flask, request, jsonify, Blueprint
from utils.functions import open_db, save_db, get_aluno
from utils.helpers import validate_and_get_aluno

app = Flask(__name__)

alunos_bp = Blueprint("alunos", __name__)

@alunos_bp.route('/alunos', methods=['GET', 'POST', 'PUT', 'DELETE'])
def alunos():
    db = open_db()
    if not db:
        jsonify(error='Error trying to open file.'), 500

    alunosList = db['alunos']
    reqMethod = request.method

    if reqMethod in ['POST', 'PUT']:
        if not request.json.get('alunos'):
            return jsonify(error='Please provide a student object as argument.'), 400

    if reqMethod == 'GET':
        aluno_req = request.args.get('aluno') # Change to endpoint

        # Returns all students
        if not aluno_req:
            return jsonify(data=alunosList)

        # Returns a specific student
        aluno, error = validate_and_get_aluno(request.args)
        if error:
            return error
        
        return jsonify(data=aluno)

    elif reqMethod == 'POST':
        for aluno in request.json['alunos']:
            aluno_name = aluno.get('name')
            if not aluno_name:
                return jsonify(error='Field "name" is required.'), 400
            
            # Put students in db
            if not get_aluno(aluno_name, db):
                alunosList.append(aluno)

        save_db(db)
        return jsonify(data=db), 201
    
    elif reqMethod == 'PUT':
        for aluno in request.json['alunos']:
            aluno_name = aluno.get('name')
            if not aluno_name:
                return jsonify(error='Field "name" is required.'), 400
                    
            for i, aluno_db in enumerate(alunosList):

                # Updates the student
                if aluno_db['name'] == aluno_name:
                    alunosList[i].update(aluno)
                    break

            else:
                # Creates a new student
                alunosList.append(aluno)
            
        save_db(db)
        return jsonify(data=db)
    
    elif reqMethod == 'DELETE':
        aluno, error = validate_and_get_aluno(request.args)
        if error:
            return error
        
        alunosList.remove(aluno)

        save_db(db)
        return "", 204 #change to 204, no content
    
    else:
        return jsonify(error='Method not allowed. Supported methods: GET, POST, PUT, DELETE.'), 405


if __name__ == "__main__":
    app.run(debug=True)