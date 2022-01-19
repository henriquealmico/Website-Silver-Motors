from app.models import BaseModel
from app.extensions import db
from flask import Blueprint


veiculo_api = Blueprint('veiculo_api', __name__)


class Veiculo(BaseModel):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    placa = db.Column(db.String(10), nullable = False, unique = True, index = True)
    modelo = db.Column(db.String(25), nullable = False)
    cor = db.Column(db.String(15), nullable = False)
    quilometragem = db.Column(db.Float, nullable = False)
    ano = db.Column(db.Integer, nullable = False)
    tipo = db.Column(db.String(20), nullable = False) #Formato do modelo. Ex: SUV, Sedan, esportivo
    preco_normal = db.Column(db.Float, nullable = False)
    preco_descontado = db.Column(db.Float, nullable = True)
    cambio = db.Column(db.String(15), nullable = False)


    def json(self): 

        return {
            "placa": self.placa,
            "modelo": self.modelo,
            "cor": self.cor,
            "quilometragem": self.quilometragem,
            "ano": self.ano,
            "tipo": self.tipo,
            "preco_normal": self.preco_normal,
            "preco_descontado": self.preco_descontado,
            "cambio": self.cambio
        }


class Carro(Veiculo):

    __tablename__ = 'carro'

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    id_pedido = db.Column(db.Integer, db.ForeignKey('pedido.id'))



class Moto(Veiculo):

    __tablename__ = 'moto'

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    id_pedido = db.Column(db.Integer, db.ForeignKey('pedido.id'))



