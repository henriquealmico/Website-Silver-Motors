from app.models import BaseModel
from app.extensions import db
from flask import Blueprint

user_api = Blueprint('user_api', __name__)


class User(BaseModel):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    idade = db.Column(db.Integer, nullable = False)
    cpf = db.Column(db.String(15), nullable = False, unique = True)
    nome = db.Column(db.String(80), nullable = False)
    email = db.Column(db.String(70), nullable = False, unique = True, index = True)
    senha = db.Column(db.String(40), nullable = False)
    endereco = db.Column(db.String(80), nullable = False)
    cidade = db.Column(db.String(20), nullable = False)
    estado = db.Column(db.String(20), nullable = False)
    cep = db.Column(db.String(15), nullable = False)
    ja_realizou_compra = db.Column(db.Boolean, nullable = False)
    como_descobriu_site = db.Column(db.String(40), nullable = False)


    id_carrinho = db.Column(db.Integer, db.ForeignKey('carrinho.id'))
    carrinho = db.relationship("Carrinho", back_populates="pedido")

    def json(self): 

        return {
            "cpf": self.cpf,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "endereco": self.endereco,
            "cidade": self.cidade,
            "estado": self.estado,
            "cep": self.cep
        }
    