from models import Pessoas

#Insere dados na tabela pessoa 
def insere_pessoas():
    pessoa = Pessoas(nome = 'Leonardo', idade = 20)
    print(pessoa)
    pessoa.save()

#Consulta dados na tabela pessoa 
def consulta_pessoas():
    pessoa = Pessoas.query.all()
    pessoa = Pessoas.query.filtered_by(nome='Leonardo').first()
    print(pessoa.idade)
    
#Altera dados na tabela pessoa    
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome ='Leonardo').first()
    pessoa.idade = 21
    pessoa.save()

#Exclui dados na tabela pessoa 
def exclui_pessoas():
    pessoa = Pessoas.query.filter_by(nome ='Felipe').first()
    pessoa.delete()


if __name__ == '__main__':
    #insere_pessoas()
    exclui_pessoas()
    consulta_pessoas()
