def criararquivo(nome = 0):
    arq = None
    try:
        arq = open(nome)
        print( f'o arquivo {nome} já existe')
        return arq 
    except:
        arq = open(nome , 'a+')
        print(f'O arquivo {nome} foi criado.')

    return arq
    
def cadastro(nome = 0 , idade = 0 , salario = 0,nome_arquivo = 0):
    arq = criararquivo(nome_arquivo)
    arq.writable(nome)
    arq.writable(idade)
    arq.writable(salario)
    arq.close

cadastro(nome = 'mateus',idade='16',salario='1500',nome_arquivo='d')





