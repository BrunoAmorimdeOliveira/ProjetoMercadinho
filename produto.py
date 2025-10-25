class protudo:

    def __init__(nome, qtd, preco):
        nome = nome
        qtd = qtd
        preco = preco


    def add_produto(qtd):
        qtd = input('Insira a Quantidade desejada: ')
        if qtd is not int:
            print('Quantidade não é número')
            if qtd > 0:
                print('Quantidade menor que zero')
