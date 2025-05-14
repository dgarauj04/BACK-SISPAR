# Blueprint request-job requisições jsonify-job respostas
from flask import Blueprint, request, jsonify
from src.model.colaborador_model import Colaborador
from src.model import db
from src.security.security import hash_senha, checar_senha
from flasgger import swag_from

bp_colaborador = Blueprint('colaborador', __name__, url_prefix='/colaborador')

dados = [
    {'id': 1, 'nome': 'Samuel Silvério', 'cargo': 'Desenvolvedor Back end', 'cracha': 'SS98510'},
    {'id': 2, 'nome': 'Karynne Moreira', 'cargo': 'Desenvolvedora Front end', 'cracha': 'KM21954'},
    {'id': 3, 'nome': 'Lucas Gomes', 'cargo': 'Desenvolvedor Full stack', 'cracha': 'LG81191'},
    {'id': 4, 'nome': 'Rafaela Alves', 'cargo': 'QA', 'cracha': 'RA99851'},
]

#GET busca informações no servidor
@bp_colaborador.route('/todos-colaboradores', methods=['GET'])
def pegar_dados_colaboradores():
    
    colaboradores = db.session.execute(
        db.select(Colaborador)
    ).scalars().all()
        
    colaboradores = [ colaborador.all_data() for colaborador in colaboradores ]
    
    return jsonify(colaboradores), 200

#POST insere informações no servidor
@bp_colaborador.route('/cadastrar', methods=['POST'])
@swag_from('../docs/colaborador/cadastrar.yml')
def cadastrar_colaborador():
    dados_request = request.get_json()
    
    novo_colaborador = Colaborador(
        nome=dados_request['nome'],
        email=dados_request['email'],
        senha=hash_senha(dados_request['senha']),
        cargo=dados_request['cargo'],
        salario=dados_request['salario'],
        cracha=dados_request['cracha']
    )

    db.session.add(novo_colaborador) 
    db.session.commit() 
    
    return jsonify( {'mensagem': 'Colaborador cadastrado com sucesso!'} ), 201


#POST insere informações no servidor
@bp_colaborador.route('/login', methods=['POST'])
def login():
    
    dados_request = request.get_json()
    email = dados_request.get('email')
    senha = dados_request.get('senha')
    
    if not email or not senha:
        return jsonify({'mensagem': 'Todos os campos devem ser preenchidos!'}), 400
     
    colaborador = db.session.execute(
        db.select(Colaborador).where(Colaborador.email == email)).scalar() 
    
    if not colaborador:
        return jsonify({'mensagem': 'O usuário não foi encontrado!'}), 404
    
    colaborador = colaborador.to_dict()    
    
    if colaborador.get('email') == email and checar_senha(senha, colaborador.get('senha')):
        return jsonify({'mensagem': 'Login realizado com sucesso!'}), 200

#PUT atualiza informações no servidor
@bp_colaborador.route('/atualizar/<int:id_colaborador>', methods=['PUT'])
def atualizar_dados_colaborador(id_colaborador):
    
    dados_colaborador = request.get_json()
    
     #Busca colaborador no banco de dados
    colaborador = db.session.execute(
        db.select(Colaborador).where(Colaborador.id == id_colaborador)
    ).scalar()
    
    if not colaborador:
        return jsonify({'mensagem': 'Colaborador nao encontrado'}), 404
    
    
 # Atualiza os campos recebidos no JSON
    if 'nome' in dados_colaborador:
        colaborador.nome = dados_colaborador['nome']
    if 'cargo' in dados_colaborador:
        colaborador.cargo = dados_colaborador['cargo']
    if 'cracha' in dados_colaborador:
        colaborador.cracha = dados_colaborador['cracha']
    if 'email' in dados_colaborador:
        colaborador.email = dados_colaborador['email']
    if 'senha' in dados_colaborador:
        colaborador.senha = hash_senha(dados_colaborador['senha'])
    if 'salario' in dados_colaborador:
        colaborador.salario = dados_colaborador['salario']

    # Commit das alterações no banco
    db.session.commit()
   

    return jsonify( {'mensagem': 'Dados do colaborador atualizados com sucesso!'}), 200

# DELETE remove colaborador do servidor
@bp_colaborador.route('/deletar/<int:id_colaborador>', methods=['DELETE'])
def deletar_colaborador(id_colaborador):
    # Busca o colaborador no banco
    colaborador = db.session.execute(
        db.select(Colaborador).where(Colaborador.id == id_colaborador)
    ).scalar()

    #Se não encontrar, retorna erro
    if not colaborador:
        return jsonify({'mensagem': 'Colaborador não encontrado!'}), 404

    #Remove o colaborador
    db.session.delete(colaborador)
    db.session.commit()

    return jsonify({'mensagem': 'Colaborador deletado com sucesso!'}), 200
