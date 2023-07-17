from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {'nome' : 'Leonardo',
     'habilidades': ['Python', 'Flask']
     },
     {
        'nome' : 'Davi',
        'habilidades' : ['Java', 'Gols em todos os jogos']
     }
]

@app.route('/dev/<int:id>/', methods = ['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        desenvolvedor = desenvolvedores[id]
        print(desenvolvedor)
        return jsonify(desenvolvedor)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados 
        return jsonify(dados)
    elif request.method == 'DELETE':
        pass




if __name__ == '__main__':
    app.run(debug = True)