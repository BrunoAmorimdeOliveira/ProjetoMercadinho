class Protudo:
    produtos = {}

    def __init__(self, nome, qtd, preco):
        self.__nome = None
        self.qtd = None
        self.preco = None


    #Getter
    @property
    def nome_produto(self):
        return self.__nome
    
    #Setter
    @nome_produto.setter
    def nome_produto(self, novo_produto):
        self.__nome = novo_produto


    def adicionar_produto(self):
        qtd = input('Insira a Quantidade desejada: ')
        if qtd is not int:
            print('Quantidade não é número')
            if qtd > 0:
                print('Quantidade menor que zero')


    def inserir_preco(self):
        self.preco = float(input('Insira o preço do produto {nome_produto}: '))
        return self.preco