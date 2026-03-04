from flask import Flask, request, jsonify
from models import db, Crianca 
from services.ai_handler import pedir_desafio_ia
import random
import app



@app.route('/cadastrar', methods=['POST'])
def cadastrar_crianca():
    
    dados = request.json
    
    nova_crianca = Crianca(
        nome=dados.get('nome'),
        idade=dados.get('idade'),
        estrelas=0 )
    
    db.session.add(nova_crianca)
    db.session.commit()
    
    return jsonify({"mensagem": f"Criança {nova_crianca.nome} cadastrada com sucesso!"}), 201

@app.route('/listar', methods=['GET'])
def listar_criancas():
    
    criancas = Crianca.query.all()
    lista = [{"id": c.id, "nome": c.nome, "estrelas": c.estrelas} for c in criancas]
    return jsonify(lista)


@app.route('/gerar_desafio_ia/<int:id_crianca>', methods=['GET'])
def gerar_desafio_ia(id_crianca):
    # 1. Busca a idade da criança no banco para a IA se adaptar
    crianca = Crianca.query.get(id_crianca)
    if not crianca:
        return jsonify({"erro": "Criança não encontrada"}), 404

    # 2. Chama a IA
    dados_ia = pedir_desafio_ia(crianca.idade)
    palavra = dados_ia['palavra'].upper()
    
    # 3. Lógica de esconder a letra correta
    lista = list(palavra)
    idx = random.randint(0, len(lista) - 1)
    letra_correta = lista[idx]
    lista[idx] = "_"
    
    return jsonify({
        "palavra_exibir": "".join(lista),
        "letra_correta": letra_correta,
        "dica": dados_ia['dica'],
        "mensagem_personagem": dados_ia['personagem_disse']
    })
