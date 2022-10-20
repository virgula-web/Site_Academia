from crypt import methods
from geral.modelo import *


@app.route("/excluir_pessoa/<string:pessoa_cpf>" , methods=['DELETE'])


def excluir_pessoa(pessoa_cpf):

    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    try:
        
        Pessoa.query.filter(Pessoa.cpf == pessoa_cpf).delete()
  
        db.session.commit()
    except Exception as e:
       
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
 
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
