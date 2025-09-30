from flask import Flask
from routes.alunos import alunos_bp
from routes.saudacao import saudacao_bp
from routes.curso import curso_bp
from routes.weather import weather_bp
from routes.gitrepo import get_repo_bp

app = Flask(__name__)

# Register routes
app.register_blueprint(alunos_bp)
app.register_blueprint(saudacao_bp)
app.register_blueprint(curso_bp)
app.register_blueprint(weather_bp)
app.register_blueprint(get_repo_bp)

if __name__ == "__main__":
    app.run(debug=True)
