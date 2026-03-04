from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Crianca(db.Model):
    __tablename__ = 'criancas'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    estrelas = db.Column(db.Integer, default=0) # Começa com 0 estrelas

    def __repr__(self):
        return f'<Crianca {self.nome} - Estrelas: {self.estrelas}>'