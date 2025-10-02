from flask import Flask, request, jsonify, Blueprint
from utils.functions import open_db, save_db, get_aluno

app = Flask(__name__)

alunos_bp = Blueprint("alunos", __name__)

@alunos_bp.route('/alunos', methods=['GET', 'POST', 'PUT', 'DELETE'])
def alunos():
    db = open_db()

    if request.method == 'GET':
        aluno_req = request.args.get('aluno')

        # Returns all students
        if not aluno_req:
            return db['alunos']
        
        # Returns a specific student
        aluno = get_aluno(aluno_req, db)
        if not aluno:
            return jsonify(error='Student not found or name malformed.'), 400
        
        return aluno

    if request.method == 'POST':
        if not request.json.get('alunos'):
            return jsonify(error='Please provide a student object as argument.'), 400
        
        for aluno in request.json.get('alunos'):
            aluno_name = aluno.get('name')
            if not aluno_name:
                return jsonify(error='Field "name" is required.'), 400
            
            # Put students in db
            if not get_aluno(aluno_name, db):
                db['alunos'].append(aluno)

        save_db(db)
        return jsonify(data=db), 201
    
    if request.method == 'PUT':
        if not request.json:
            return jsonify(error='Please provide a student JSON as argument.'), 400

        for aluno in request.json['alunos']:
            aluno_name = aluno.get('name')
            if not aluno_name:
                return jsonify(error='Field "name" is required.'), 400
            
            for i, aluno_db in enumerate(db['alunos']):

                # Updates the student
                if aluno_db['name'] == aluno_name:
                    db['alunos'][i].update(aluno)
                    break

            else:
                # Creates a new student
                db['alunos'].append(aluno)
            
        save_db(db)
        return jsonify(data=db)
    
    if request.method == 'DELETE':
        aluno_req = request.args.get('aluno')
        if not aluno_req:
            return jsonify(error='Please provide a student name.'), 400
        
        aluno = get_aluno(aluno_req, db)
        if not aluno:
            return jsonify(error='Student not found or name malformed.'), 404
        
        # Removes the student
        db['alunos'].remove(aluno)

        save_db(db)
        return jsonify(data=db)


if __name__ == "__main__":
    app.run(debug=True)