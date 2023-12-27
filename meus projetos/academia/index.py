from indexfunc import *

print('''
[1] Criar arquivo
[2] cadastrar 
[3] ver pessoas cadastradas''')    

op = int(input("ESCOLHA UMA OPÇÃO:"))

if op < 1 or op > 3:
    print('Não existe essa opção.')
else:
    while True:
        if op == 1:
            nome = str(input('Dê UM NOME PARA O ARQUIVO QUE VAI SER CRIADO:'))
            arquivo = criararquivo(nome + '.txt')
        if op ==2:
            nome = str(input('DIGITE O SEU NOME:'))
            idade = int(input('DIGITE A SUA IDADE:'))
            salario = float(input('DIGITE O SEU SALARIO'))
            cadastrar(nome,idade,salario)


    
