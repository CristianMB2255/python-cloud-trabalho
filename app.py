from flask import Flask, request, jsonify
import json

app = Flask(__name__)

DB_FILE = 'alunos.json'

# Checks the existence of a student
def get_aluno(aluno_name, db):
    for aluno in db['alunos']:
        if (aluno['name']) == aluno_name:
                return aluno
    return False

# Opens file
def open_db():
    with open(DB_FILE) as fr:
        return json.load(fr)
    if not fr:
        return jsonify(error='Error trying to open file.'), 500
    
#Saves database
def save_db(db):
    with open(DB_FILE, 'w') as fw:
        json.dump(db, fw, indent=4)


@app.route('/alunos', methods=['GET', 'POST'])
def aluno():
    db = open_db()

    if request.method == 'GET':

        # Returns all the students if no args
        aluno_req = request.args.get('aluno')
        if not aluno_req:
            return db['alunos']
        
        # Returns a specific student
        aluno = get_aluno(aluno_req, db)
        if not aluno:
            return jsonify(error='Student not found or name malformed.'), 400
        
        return aluno

    if request.method == 'POST':
        if not request.json or not request.json.get('alunos'):
            return jsonify(error='Please pass a student JSON as argument.'), 400
        
        # Put students in db
        for aluno in request.json.get('alunos'):
            if not get_aluno(aluno['name'], db):
                db['alunos'].append(aluno)

        save_db(db)
        return jsonify(data=db)


if __name__ == "__main__":
    app.run(debug=True)