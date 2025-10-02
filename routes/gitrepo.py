from flask import Flask, jsonify, request, Blueprint
from utils.functions import open_db, get_aluno
import requests

app = Flask(__name__)

get_repo_bp = Blueprint("/github-repo", __name__)

@get_repo_bp.route('/github-repo')
def github_repo():
    aluno_req = request.args.get('aluno')
    if not aluno_req:
        return jsonify(error='Please provide a student name.'), 400

    db = open_db()
    
    aluno = get_aluno(aluno_req, db)
    if not aluno:
        return jsonify(error='Student not found or name malformed.'), 404

    repo_link = aluno.get('github_repo')
    if not repo_link:
        return jsonify(error='Student does not have a registered repo.'), 400

    response = requests.get(repo_link)
    if response.status_code != 200:
        return jsonify(error='Repository not found.'), 400
    
    data = response.json()

    result = {
        "name": data.get("name"),
        "description": data.get("description"),
        "stars": data.get("stargazers_count")
    }

    return jsonify(result)