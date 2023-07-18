import json
from flask import Flask, request
from habilidades import Habilidades
from flask_restful import Resource , Api


app = Flask (__name__)
api = Api(app)

desenvolvedores = [
    {
        'id' : 0,
        'nome' : 'Leonardo',
        'habilidades': ['Python', 'Flask']
     },
     {
        'id' : 1,
        'nome' : 'Davi',
        'habilidades' : ['Meia - atacante', 'Gols em todos os jogos']
     }
]

#devolve um desenvolvedor pelo ID, altera e deleta desenvolvedor 
class Desenvolvedor(Resource):
    def get(self,id):
       try:
            response = desenvolvedores[id]
       except IndexError:
        mensagem = 'Desenvolvedor de id {} não existe'.format(id)
        response = {'status': 'erro', 'mensagem': mensagem}
       except Exception:
        mensagem = 'Erro desconhecido, Procure o administrador da API'
        response = {'status': 'erro', 'mensagem': mensagem}
       return response
    
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados
    
    def delete(self,id):
        desenvolvedores.pop(id)
        return {'status' : 'sucesso', 'mensagem' : 'Registro Excluido'}
    

#Lista todos os desenvolvedores e permite registrar um novo desenvolvedor 
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]
        
#como se fosse os decoradores que ficam na parte de cima das defs '@app.route....'  
api.add_resource(Desenvolvedor, '/dev/<int:id>/')    
api.add_resource(ListaDesenvolvedores, '/dev/')
app.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug= True)