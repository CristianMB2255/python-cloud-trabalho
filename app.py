from flask import Flask
from routes.alunos import alunos_bp
from routes.saudacao import saudacao_bp
from routes.curso import curso_bp

app = Flask(__name__)

# Register routes
app.register_blueprint(alunos_bp)
app.register_blueprint(saudacao_bp)
app.register_blueprint(curso_bp)

if __name__ == "__main__":
    app.run(debug=True)
