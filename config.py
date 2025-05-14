from os import environ #Traz para o arquivo o acesso as variáveis de ambiente
from dotenv import load_dotenv #Traz a funçõa para carregar as variaveis de ambiente nesse arquivo

#Carrega as variaveis de ambiente para este arquivo
load_dotenv()

class Config():
    SQLALCHEMY_DATABASE_URI = environ.get('URL_DATABASE_DEV') #Pega a variavel de ambiente e atribui a ela a variavel SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False #Otimiza o acesso ao banco de dados 
    print("URL DO BANCO:", environ.get('URL_DATABASE_DEV'))
