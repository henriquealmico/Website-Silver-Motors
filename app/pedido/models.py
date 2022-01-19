from app.models import BaseModel
from app.extensions import db
from flask import Blueprint

pedido_api = Blueprint('pedido_api', __name__)


class BasePedidoCarrinho(BaseModel):

    __abstract__ = True
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    modelo_entrega = db.Column(db.String(15), nullable = False)
    preco_entrega = db.Column(db.String(15), nullable = False)
    quantidade_itens = db.Column(db.Integer, nullable = False) 
    preco_total = db.Column(db.Float, nullable=False)
    data_pedido = db.Column(db.DateTime, nullable = False)
    forma_pagamento = db.Column(db.String(15), nullable = False)


    def json(self): 

        return {
            "preco_total": self.preco_total,
            "data_pedido": self.data_pedido,
            "forma_pagamento": self.forma_pagamento,
            "modelo_entrega": self.modelo_entrega,
            "preco_entrega": self.preco_entrega,
            "quantidade_itens": self.quantidade_itens
        }



class Pedido(BasePedidoCarrinho):

    __tablename__ = 'pedido'

    pagamento_confirmado = db.Column(db.Boolean, nullable = False)

    user_id = db.Column(db.ForeignKey('user.id'))
    carros = db.relationship("Carro")
    motos = db.relationship("Moto")
    id_cupom = db.Column(db.Integer, db.ForeignKey('cupom.id'))
   
    

class Carrinho(BasePedidoCarrinho):

    __tablename__ = 'carrinho'


    user_id = db.Column(db.ForeignKey('user.id'))
    id_carro = db.Column(db.ForeignKey('carro.id'))
    id_moto = db.Column(db.ForeignKey('moto.id'))
    id_cupom = db.Column(db.Integer, db.ForeignKey('cupom.id'))


