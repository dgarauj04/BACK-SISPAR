from flask import Blueprint, request, jsonify
from src.model import db
from src.model.reembolso_model import Reembolso
from src.model.colaborador_model import Colaborador
from flasgger import swag_from

bp_reembolso = Blueprint('reembolso', __name__, url_prefix='/refunds')


# Rota para solicitar reembolso (POST)
@bp_reembolso.route('/new', methods=['POST'])
@swag_from('../docs/reembolso/registrar.yml')
def solicitar_reembolso():
    dados = request.get_json()

    colaborador = db.session.execute(
        db.select(Colaborador)
    ).scalars().first()

    if not colaborador:
        return jsonify({'mensagem': 'Nenhum colaborador cadastrado!'}), 404

    novo_reembolso = Reembolso(
        colaborador=dados['colaborador'],
        empresa=dados['empresa'],
        num_prestacao=dados['nPrestacao'],
        descricao=dados.get('descricao'),
        data=dados.get('data'),
        tipo_reembolso=dados['tipoReembolso'],
        centro_custo=dados['centroCusto'],
        ordem_interna=dados.get('ordemInterna'),
        divisao=dados.get('divisao'),
        pep=dados.get('pep'),
        moeda=dados['moeda'],
        distancia_km=dados.get('distanciaKm'),
        valor_km=dados.get('valorKm'),
        valor_faturado=dados['valorFaturado'],
        despesa=dados.get('despesa'),
        status=dados.get('status', 'Em analise')
    )

    db.session.add(novo_reembolso)
    db.session.commit()

    return jsonify({"mensagem": "Reembolso solicitado com sucesso!"}), 201


# Rota para buscar reembolso por número de prestação (GET)
@bp_reembolso.route('/get-refunds/<int:num_prestacao>', methods=['GET'])
@swag_from('../docs/reembolso/buscar_reembolso.yml')
def buscar_reembolso(num_prestacao):
    reembolso = Reembolso.query.filter_by(num_prestacao=num_prestacao).first()

    if not reembolso:
        return jsonify({"mensagem": "Reembolso não encontrado."}), 404

    resultado = {
        "id": reembolso.id,
        "colaborador": reembolso.colaborador,
        "empresa": reembolso.empresa,
        "num_prestacao": reembolso.num_prestacao,
        "descricao": reembolso.descricao,
        "data": reembolso.data.strftime('%Y-%m-%d'),
        "tipo_reembolso": reembolso.tipo_reembolso,
        "centro_custo": reembolso.centro_custo,
        "ordem_interna": reembolso.ordem_interna,
        "divisao": reembolso.divisao,
        "pep": reembolso.pep,
        "moeda": reembolso.moeda,
        "distancia_km": reembolso.distancia_km,
        "valor_km": str(reembolso.valor_km) if reembolso.valor_km else None,
        "valor_faturado": str(reembolso.valor_faturado),
        "despesa": str(reembolso.despesa) if reembolso.despesa else None,
        "status": reembolso.status
    }

    return jsonify(resultado, {"mensagem": "Reembolsos encontrados."}), 200

# Rota para atualizar um reembolso (PUT)
@bp_reembolso.route('/update/<int:id_reembolso>', methods=['PUT'])
@swag_from('../docs/reembolso/atualizar_reembolso.yml')
def atualizar_reembolso(id_reembolso):
    dados_request = request.get_json()
    
    reembolso = db.session.execute(
    db.select(Reembolso).where(Reembolso.id == id_reembolso)
    ).scalar()

    if not reembolso:
        return jsonify({"mensagem": "Reembolso não encontrado."}), 404

    # Atualiza cada campo individualmente com verificação explícita
    if 'colaborador' in dados_request:
        reembolso.colaborador = dados_request['colaborador']
    if 'empresa' in dados_request:
        reembolso.empresa = dados_request['empresa']
    if 'nPrestacao' in dados_request:
        reembolso.num_prestacao = int(dados_request['nPrestacao'])
    if 'descricao' in dados_request:
        reembolso.descricao = dados_request['descricao']
    if 'tipoReembolso' in dados_request:
        reembolso.tipo_reembolso = dados_request['tipoReembolso']
    if 'data' in dados_request:
        reembolso.data = dados_request['data']
    if 'centroCusto' in dados_request:
        reembolso.centro_custo = dados_request['centroCusto']
    if 'ordemInterna' in dados_request:
        reembolso.ordem_interna = dados_request['ordemInterna']
    if 'divisao' in dados_request:
        reembolso.divisao = dados_request['divisao']
    if 'pep' in dados_request:
        reembolso.pep = dados_request['pep']
    if 'distanciaKm' in dados_request:
        reembolso.distancia_km = float(dados_request['distanciaKm'])
    if 'valorKm' in dados_request:
        reembolso.valor_km = float(dados_request['valorKm'])
    if 'valorFaturado' in dados_request:
        reembolso.valor_faturado = float(dados_request['valorFaturado'])
    if 'despesa' in dados_request:
        reembolso.despesa = float(dados_request['despesa'])
    if 'status' in dados_request:
        reembolso.status = dados_request['status']
    if 'moeda' in dados_request:
        reembolso.moeda = dados_request['moeda']

    db.session.commit()

    return jsonify({"mensagem": "Reembolso atualizado com sucesso!"}), 200

#Rota para deletar um reembolso (DELETE)
@bp_reembolso.route('/delete/<int:id_reembolso>', methods=['DELETE'])
@swag_from('../docs/reembolso/apagar.yml')
def deletar_reembolso(id_reembolso):
    
    reembolso = db.session.execute(
    db.select(Reembolso).where(Reembolso.id == id_reembolso)
    ).scalar()

    if not reembolso:  # ← Esta linha deve estar alinhada com o início do bloco
        return jsonify({"mensagem": "Reembolso não encontrado."}), 404

    db.session.delete(reembolso)
    db.session.commit()

    return jsonify({"mensagem": "Reembolso deletado com sucesso!"}), 200