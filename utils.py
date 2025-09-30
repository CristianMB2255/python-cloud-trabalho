import json

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