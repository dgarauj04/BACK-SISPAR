from src.model import db #Traz a instancia SQLAlchemy para este arquivo
from sqlalchemy.schema import Column #Traz o recurso que transforma atributos em colunas 
from sqlalchemy.types import String, DECIMAL, Integer #Traz o recurso que identifica os tipos de dados para as colunas

class Colaborador(db.Model): #db.Model serve para criar a tabela
    __tablename__ = 'tb_colaboradores' #nome da tabela
    
#Atributos da tabela
    id = Column(Integer, primary_key=True, autoincrement=True) #id INT AUTO_INCREMENT PRIMARY KEY
    nome = Column(String(255)) #nome VARCHAR(255)
    email = Column(String(150)) #email VARCHAR(150)
    senha = Column(String(255)) #senha VARCHAR(255)
    cargo = Column(String(100)) #cargo VARCHAR(100)
    salario = Column(DECIMAL(10,2)) #salario DECIMAL(10,2)
    cracha = Column(String(50)) #cracha VARCHAR(6)
    
#CONSTRUTOR DE OBJETOS
    def __init__ (self, nome, email, senha, cargo, salario, cracha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cargo = cargo
        self.salario = salario      
        self.cracha = cracha

#METODOS 
    def to_dict(self) -> dict: 
        return {
            'email': self.email,
            'senha': self.senha
        }
        
    def all_data(self) -> dict:
        return {
            'id': self.id,
            'nome': self.nome,
            'cargo': self.cargo,
            'salario': self.salario
        }