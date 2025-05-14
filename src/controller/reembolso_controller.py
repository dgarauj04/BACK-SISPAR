from flask import Blueprint, request, jsonify
from src.model import db
from src.model.reembolso_model import Reembolso
from src.model.colaborador_model import Colaborador

bp_reembolso = Blueprint('reembolso', __name__, url_prefix='/refunds')


# Rota para solicitar reembolso (POST)
@bp_reembolso.route('/new', methods=['POST'])
def solicitar_reembolso():
    dados = request.get_json()

    colaborador = db.session.execute(
        db.select(Colaborador)
    ).scalars().first()

    if not colaborador:
        return jsonify({'mensagem': 'Nenhum colaborador cadastrado!'}), 404

    novo_reembolso = Reembolso(
        id_colaborador=colaborador.id,
        colaborador=dados['colaborador'],
        empresa=dados['empresa'],
        num_prestacao=dados['nPrestacao'],
        descricao=dados.get('motivo'),
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
@bp_reembolso.route('/<int:num_prestacao>', methods=['GET'])
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

    return jsonify(resultado), 200

# Rota para atualizar um reembolso (PUT)
@bp_reembolso.route('/update/<int:num_prestacao>', methods=['PUT'])
def atualizar_reembolso(num_prestacao):
    dados_request = request.get_json()

    reembolso = Reembolso.query.filter_by(num_prestacao=num_prestacao).first()

    if not reembolso:
        return jsonify({"mensagem": "Reembolso não encontrado."}), 404

    # Atualiza apenas os campos enviados na requisição
    for chave, valor in dados_request.items():
        if hasattr(reembolso, chave):
            setattr(reembolso, chave, valor)

    db.session.commit()

    return jsonify({"mensagem": "Reembolso atualizado com sucesso!"}), 200

#Rota para deletar um reembolso (DELETE)
@bp_reembolso.route('/delete/<int:num_prestacao>', methods=['DELETE'])
def deletar_reembolso(num_prestacao):
    reembolso = Reembolso.query.filter_by(num_prestacao=num_prestacao).first()

    if not reembolso:
        return jsonify({"mensagem": "Reembolso não encontrado."}), 404

    db.session.delete(reembolso)
    db.session.commit()

    return jsonify({"mensagem": "Reembolso deletado com sucesso!"}), 200
