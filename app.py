from flask import Flask, request
from models import db
import os


app = Flask(__name__)

# Configuração do Banco de Dados
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Cria as tabelas automaticamente
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True, port=8080)

