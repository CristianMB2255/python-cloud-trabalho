from flask import Flask, request
import json

app = Flask(__name__)

def get_aluno(aluno_name, db):
    for aluno in db['alunos']:
        if (aluno['name']) == aluno_name:
                return aluno
        return False

@app.route('/alunos', methods=['GET', 'POST'])
def aluno():
    if request.method == 'GET':
        aluno_req = request.args.get('aluno')

        if not aluno_req:
            return({ 'error': 'Please pass a student name as an argument.', 'status': 400 })

        with open('alunos.json') as f:
            db = json.load(f)

        if not f:
            return({ 'error': 'Error trying to open the file.', 'status': 500 })
        

        aluno = get_aluno(aluno_req, db)

        if not aluno:
            return({ 'error': 'Student not found or name malformed.', 'status': 400 })
        
        return aluno

    if request.method == 'POST':
        if not request.json:
            return({ 'error': 'Please pass a student JSON as argument.', 'status': 400 })
         
        with open('alunos.json') as fr:
            data = json.load(fr)

        if not fr:
            return({ 'error': 'Error trying to open the file.', 'status': 500 })
        
        for aluno in request.json["alunos"]:
            data["alunos"].append(aluno)

        with open('alunos.json', 'w') as fw:
            data = json.dump(data, fw, indent=4)

        return data


if __name__ == "__main__":
    app.run(debug=True)