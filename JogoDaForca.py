import random

des_forca = ['''
 +---+
 |   |
     |
     |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
     |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
 |   |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |    
=========
''']

sorteio = []#lista que vai guardar a palavra sorteada de cada categoria
letra = []#lista que vai guardar a letra chutada pelo usuario
qtde_letra = []#lista que vai guardar a quantidade de letras que tem na palavra sorteada mas em '_'
digitados = []#lista que vai guardar todas as letras que o usuario já digitou

print('''
===============================
| BEM-VINDO AO JOGO DA FORCA! |
===============================''')

resp = input("Você deseja jogar o jogo da forca?(sim/nao)\n").lower()
if resp != 'sim' and resp !='nao':
    print("Não tem essa opção!")
    resp = input("Você deseja jogar o jogo da forca?(sim/nao)\n").lower()
while resp == 'sim':#Aqui começa a repetição de acordo com a resposta do usuario
    print("Qual modo você escolhe jogar?")
    modo = input("Fruta\nComida\nPaises\n").lower()#Usuario escolhe qual o modo ele deseja jogar

    if modo == 'fruta':#Se caso ele desejar jogar o modo de frutas entra nesse if
        op = ['banana','morango','cereja','amora','abacaxi','goiaba','jabuticaba','laranja'] #Lista de frutas
        sorteio = random.choice(op) #aqui sorteia uma das opções da lista acima

    elif modo == 'comida':#Se caso o usuario desejar jogar o modo de comida
        op = ['lasanha','strogonoff','feijoada','moqueca','galinhada','acaraje'] #lista de comidas
        sorteio = random.choice(op) #aqui sorteia uma das opções da lista acima

    elif modo == 'paises':#se o usuario desejar jogar modo de paises
        op = ['brasil','italia','alemanha','argentina','uruguai','canada','mexico','portugal']#lista de paises
        sorteio = random.choice(op)#aqui sorteia uma das opções da lista acima

    else: #se caso a opção que o usuario digitou não existir cai nesse else
        print("Opção não encontrada!\n")
        print("Digite o modo que você deseja jogar novamente: ")
        modo = input("Fruta\nComida\nPaises\n").lower()

    cont=0 #contador para saber a quantidade de erros
    qtde_letra = '_' * len(sorteio)#vai trocar a quantidade de letras por '_'
    i=0#contador usado no for
    cont_acerto = 0 #conta quantas vezes o usuario acertou

    print(des_forca[cont])  #exibição do desenho da forca na posição 0
    for i in range(len(sorteio)):#for para exibir a quantidade de '_'
        print(qtde_letra[i], end=' ')
    while cont<len(des_forca) and cont_acerto<len(sorteio):#enquanto o usuario não errar e nem acertar todas as vezes o jogo ainda roda
        if cont < 6:
            letra = str(input("\nDigite uma letra: ")).lower()#deixa o usuario digitar uma letra
            while letra in digitados:#se caso a letra que o usuario digitou já foi digitada entra nessa repetição até ele digitar uma letra diferente
                print("Essa letra já foi digitada!")
                letra = str(input("Digite uma nova letra: ")).lower()  #deixa o usuario digitar uma letra novamente
            digitados.append(letra)#adiciona a letra que o usuario digitou na lista para checar se ele já digitiu ela antes

        if letra in sorteio: #verifica se a letra tem na palavra
            pos = 0 #vai ser usado para descobrir a  posição da letra
            while pos<len(sorteio): #vai rodar enquanto pos for menor que o tamanho da palavra sorteada
                if letra == sorteio[pos]: #descobrindo a posição para inserir a letra
                    qtde_letra = list(qtde_letra) #tranforma a variavel que armazena os '_' para lista
                    qtde_letra[pos] = letra #troca o '_' na posição que achou a letra
                    pos = pos + 1 #posição que achou a letra na palavra
                    cont_acerto = cont_acerto + 1 #para saber quando o usuario acertou todas as letras
                else:
                    pos = pos + 1#posição que achou a letra na palavra
        else:
            cont = cont + 1 #conta quantos erros o usuario teve
        if cont < 6:
            print(des_forca[cont])

        if cont < 6 and cont_acerto < len(sorteio): #exibe a lista da palavra na posição atual
            for i in range(len(qtde_letra)):
                print(qtde_letra[i], end=' ')

    if cont > 6:#exibe a palavra e a forca na posição atual do fim do jogo
        print(des_forca[cont-1])#exibição do desenho da forca
        for i in range(len(qtde_letra)):
            print(qtde_letra[i], end=' ')
        print("\nVocê perdeu a palavra era {}".format(sorteio))#print para quando a pessoa errar todas as tentativas

    if cont_acerto == len(sorteio):#if de comparação para verificar se o usuario acertou todas as letras da palavra
        for i in range(len(qtde_letra)):
            print(qtde_letra[i], end=' ')#exibe a lista da palavra na posição atual
        print("\nParabens você ganhou!")#exibe quando o usuario acertar todas as letras que tem na palavra

    digitados.clear()#limpa a lista de caracteres digitados

    resp = input("\nVocê deseja jogar novamente?(sim/nao)").lower()#pergunta se o usuario deseja jogar novamente

if resp == 'nao':#Se a usuario digitar 'nao' o jogo termina e exibe o print a baixo
    print('''
===================
| JOGO ENCERRADO! |
===================''')