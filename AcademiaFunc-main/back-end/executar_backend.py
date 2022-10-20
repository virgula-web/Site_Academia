from geral.modelo import *
from rotas.rota_listar import *
from rotas.rota_incluir import *
from rotas.rota_update import *
from rotas.rota_delete import *
from flask_ipban import IpBan

@app.route("/")
def inicio():
    return 'Aqui esta o nosso inicio'

app.run(debug=True, host="0.0.0.0")