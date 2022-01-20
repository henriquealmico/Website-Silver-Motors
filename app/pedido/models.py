from app.models import BaseModel
from app.extensions import db
from flask import Blueprint

pedido_api = Blueprint('pedido_api', __name__)


class BasePedidoCarrinho(BaseModel):

    __abstract__ = True
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    modelo_entrega = db.Column(db.String(15), nullable = False)
    preco_entrega = db.Column(db.String(15), nullable = False)
    prazo_entrega = db.Column(db.String(15), nullable = False)
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
    data_confirmacao_pagamento = db.Column(db.DateTime, nullable = True)
    valor_de_entrada = db.Column(db.Float, nullable = True)
    numero_parcelas = db.Column(db.Integer, nullable = True)

    #One-to-One Relationships
    id_carrinho = db.Column(db.Integer, db.ForeignKey('carrinho.id'))
    carrinho = db.relationship("Carrinho", back_populates="pedido")


class Carrinho(BasePedidoCarrinho):

    __tablename__ = 'carrinho'


    #One-to-One Relationships
    user = db.relationship("User", back_populates="carrinho", uselist=False)
    cupom = db.relationship("Cupom", back_populates="carrinho", uselist=False)
    pedido = db.relationship("Pedido", back_populates="carrinho", uselist=False)

    #One-to-Many Relationships
    carro = db.relationship("Carro")
    moto = db.relationship("Moto")
    
    


