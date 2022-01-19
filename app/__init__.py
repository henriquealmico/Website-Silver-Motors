from flask import Flask
from .config import Config
from .extensions import db, migrate
from app.user.models import user_api
from app.cupons.models import cupom_api
from app.veiculos.models import veiculo_api
from app.pedido.models import pedido_api


def create_app():

    app = Flask(__name__, instance_relative_config=True)
    app.config['SECRET_KEY'] = 'Fluxo'
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    #from .views import views
    #from .auth import auth

    #app.register_blueprint(views, url_prefix = '/')
    #app.register_blueprint(auth, url_prefix = '/')

    app.register_blueprint(user_api)
    app.register_blueprint(cupom_api)
    app.register_blueprint(veiculo_api)
    app.register_blueprint(pedido_api)
    
    return app

