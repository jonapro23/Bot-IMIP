from flask import Flask
from models import db, Crianca
import os

app = Flask(__name__)

# Configuração do caminho do banco de dados SQLite
# Ele criará um arquivo chamado 'database.db' na pasta do seu projeto
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o banco com o app
db.init_app(app)

# Comando para criar o banco de dados e as tabelas se não existirem
with app.app_context():
    db.create_all()
    print("Banco de dados e tabelas criados com sucesso!")

@app.route('/')
def index():
    return "Banco de dados pronto para o IMIP!"

if __name__ == '__main__':
    app.run(debug=True)