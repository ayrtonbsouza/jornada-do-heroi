from random import randint, randrange


def sala_1():
    opcao = input(
        'Sala 1: \nSelecione um caminho: \n 1 - Direita \n 2 - Esquerda\n')
    if opcao == '1':
        sala_2()
    elif opcao == '2':
        sala_3()


def sala_2():
    opcao = input(
        'Sala 2: \nSelecione um caminho: \n 1 - Direita \n 2 - Esquerda\n')
    if opcao == '1':
        sala_3()
    elif opcao == '2':
        sala_4()


def sala_3():
    opcao = input(
        'Sala 3: \nSelecione um caminho: \n 1 - Direita \n 2 - Esquerda\n')
    if opcao == '1':
        sala_4()
    elif opcao == '2':
        sala_5()


def sala_4():
    opcao = input(
        'Sala 4: \nSelecione um caminho: \n 1 - Direita \n 2 - Esquerda\n')
    if opcao == '1':
        sala_5()
    elif opcao == '2':
        sala_6()


def sala_5():
    opcao = input(
        'Sala 5: \nSelecione um caminho: \n 1 - Direita \n 2 - Esquerda\n')
    if opcao == '1':
        sala_6()
    elif opcao == '2':
        sala_7()


def sala_6():
    print('Sala 6: \nAqui você só tem um caminho, o da Esquerda\n, seguindo para próxima sala.\n')
    sala_8()


def sala_7():
    opcao = input(
        'Sala 7: \nSelecione um caminho: \n 1 - Direita \n 2 - Esquerda\n')
    if opcao == '1':
        sala_8()
    elif opcao == '2':
        sala_9()


def sala_8():
    opcao = input(
        'Sala 8: \nSelecione um caminho: \n 1 - Direita \n 2 - Esquerda\n')
    if opcao == '1':
        sala_9()
    elif opcao == '2':
        portal()


def sala_9():
    print('Sala 9: \nParabéns, você venceu!\n')


def portal():
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


sala_1()
