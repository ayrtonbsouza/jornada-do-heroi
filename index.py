from random import randint, randrange


def sala_1():
    opcao = input('Selecione um caminho: \n 1 - Direita \n 2 - Esquerda')
    if opcao == 1:
        sala_2()
    elif opcao == 2:
        sala_3()


def sala_2():
    opcao = input('Selecione um caminho: \n 1 - Direita \n 2 - Esquerda')
    if opcao == 1:
        sala_3()
    elif opcao == 2:
        sala_4()


def sala_3():
    opcao = input('Selecione um caminho: \n 1 - Direita \n 2 - Esquerda')
    if opcao == 1:
        sala_4()
    elif opcao == 2:
        sala_5()


def sala_4():
    opcao = input('Selecione um caminho: \n 1 - Direita \n 2 - Esquerda')
    if opcao == 1:
        sala_5()
    elif opcao == 2:
        sala_6()


def sala_5():
    opcao = input('Selecione um caminho: \n 1 - Direita \n 2 - Esquerda')
    if opcao == 1:
        sala_6()
    elif opcao == 2:
        sala_7()


def sala_6():
    print('Aqui você só tem um caminho, o da esquerda, seguindo para próxima sala.')
    sala_8()


def sala_7():
    opcao = input('Selecione um caminho: \n 1 - Direita \n 2 - Esquerda')
    if opcao == 1:
        sala_8()
    elif opcao == 2:
        sala_9()


def sala_8():
    opcao = input('Selecione um caminho: \n 1 - Direita \n 2 - Esquerda')
    if opcao == 1:
        sala_9()
    elif opcao == 2:
        portal()


def sala_9():
    print('Parabéns, você venceu!')


def portal():
    randomico = randint(1, 5)
    print('Você caiu em um portal, que randomicamente te levou à sala ', randomico)
    if randomico == 1:
        sala_1()
    elif randomico == 2:
        sala_2()
    elif randomico == 3:
        sala_3()
    elif randomico == 4:
        sala_4()
    elif randomico == 5:
        sala_5()
