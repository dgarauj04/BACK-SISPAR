# RESPONSÁVEL PELA CRIAÇÃO DA INSTÂNCIA E CONFIGURAR O FLASK
# CREATE_APP() -> 
from flask import Flask
from src.controller.colaborador_controller import bp_colaborador
from src.model import db
from config import Config

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp_colaborador)
    
    app.config.from_object(Config) # Trouxemos a configuração do ambiente de desenvolvimento
    db.init_app(app) # Se inicia a conexão com o banco de dados
    
    with app.app_context():
        db.create_all() #Cria as tabelas caso elas não existam

    return app