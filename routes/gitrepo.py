from flask import Flask, jsonify, request, Blueprint
from utils.helpers import validate_and_get_aluno
import requests

app = Flask(__name__)

get_repo_bp = Blueprint("/github-repo", __name__)

@get_repo_bp.route('/github-repo')
def github_repo():
    aluno, error = validate_and_get_aluno(request.args)
    if error:
        return error

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