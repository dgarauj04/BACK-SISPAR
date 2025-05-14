#RESPONSÁVEL PELA CRIAÇÃo DA APLICACAO FLASk
from flask import Flask
from src.controller.colaborador_controller import bp_colaborador
from src.controller.reembolso_controller import bp_reembolso
from src.model import db
from config import Config
from flask_cors import CORS
from flasgger import Swagger


swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec',
                "route": '/apispec.json/',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/apidocs/"
    }

def create_app():
    app = Flask(__name__)
    CORS(app, origins='*') #Ativa o CORS para todas as rotas da API
    app.register_blueprint(bp_colaborador)
    app.register_blueprint(bp_reembolso)
    
    app.config.from_object(Config) #Configuração do ambiente de desenvolvimento
    
    db.init_app(app) #Inicia a conexão com o banco de dados
#Instancia o Swagger e adiciona as configurações
    with app.app_context():
        db.create_all() #Code que Cria as tabelas caso elas não existam
    Swagger(app, config=swagger_config)
    
    return app