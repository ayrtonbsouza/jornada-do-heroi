from random import randint, randrange

rodada = 0


def sala_1():
    opcao = input(
        'Sala 1: \nSelecione um caminho: \n 1 - Direita \n 2 - Esquerda\n')
    if opcao == '1' and rodada < 7:
        sala_2()
    elif opcao == '2' and rodada < 7:
        sala_3()
    else:
        fim_de_jogo()


def sala_2():
    global rodada
    rodada += 1
    opcao = input(
        'Sala 2: \nSelecione um caminho: \n 1 - Direita \n 2 - Esquerda\n')
    if opcao == '1' and rodada < 7:
        sala_3()
    elif opcao == '2' and rodada < 7:
        sala_4()
    else:
        fim_de_jogo()


def sala_3():
    global rodada
    rodada += 1
    opcao = input(
        'Sala 3: \nSelecione um caminho: \n 1 - Direita \n 2 - Esquerda\n')
    if opcao == '1' and rodada < 7:
        sala_4()
    elif opcao == '2' and rodada < 7:
        sala_5()
    else:
        fim_de_jogo()


def sala_4():
    global rodada
    rodada += 1
    opcao = input(
        'Sala 4: \nSelecione um caminho: \n 1 - Direita \n 2 - Esquerda\n')
    if opcao == '1' and rodada < 7:
        sala_5()
    elif opcao == '2' and rodada < 7:
        sala_6()
    else:
        fim_de_jogo()


def sala_5():
    global rodada
    rodada += 1
    opcao = input(
        'Sala 5: \nSelecione um caminho: \n 1 - Direita \n 2 - Esquerda\n')
    if opcao == '1' and rodada < 7:
        sala_6()
    elif opcao == '2' and rodada < 7:
        sala_7()
    else:
        fim_de_jogo()


def sala_6():
    global rodada
    rodada += 1
    print('Sala 6: \nAqui você só tem um caminho, o da Esquerda\n, seguindo para próxima sala.\n')
    if rodada < 7:
        sala_8()
    else:
        fim_de_jogo()


def sala_7():
    global rodada
    rodada += 1
    opcao = input(
        'Sala 7: \nSelecione um caminho: \n 1 - Direita \n 2 - Esquerda\n')
    if opcao == '1' and rodada < 7:
        sala_8()
    elif opcao == '2' and rodada < 7:
        sala_9()
    else:
        fim_de_jogo()


def sala_8():
    global rodada
    rodada += 1
    opcao = input(
        'Sala 8: \nSelecione um caminho: \n 1 - Direita \n 2 - Esquerda\n')
    if opcao == '1' and rodada < 7:
        sala_9()
    elif opcao == '2' and rodada < 7:
        portal()
    else:
        fim_de_jogo()


def sala_9():
    global rodada
    rodada += 1
    print('Sala 9: \nParabéns, você venceu!\n')


def portal():
    global rodada
    rodada += 1
    randomico = randint(1, 5)
    print('Você caiu em um portal, que randomicamente te levou à sala ', randomico, '\n')
    if randomico == '1':
        sala_1()
    elif randomico == '2':
        sala_2()
    elif randomico == '3':
        sala_3()
    elif randomico == '4':
        sala_4()
    elif randomico == '5':
        sala_5()


def fim_de_jogo():
    print('Game Over:\nVocê atingiu 7 jogadas antes de chegar ao final.')


sala_1()
