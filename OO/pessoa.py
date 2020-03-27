class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=".", idade=45):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f"Olá, meu nome é {self.nome} !!!"

    @staticmethod
    def metodo_estatico():
        return 198

    @classmethod
    def mostra_olhos(cls):
        return f' A {cls.nome} tem {cls.olhos} olhos!!! '

class Mulher(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar(self)  # chama o metodo da classe pai.
        return f'{cumprimentar_da_classe} Seja bem vindo .'

class Mutante(Pessoa):
    olhos = 3



if __name__ == "__main__":
    f = Pessoa(nome='Christiane')
    p = Mutante(f, nome='Theresinha')
    print(Pessoa.cumprimentar(p))  # chamada do método
    print(p.cumprimentar())  # chamada do método
    print(p.nome)  # acesso ao parâmetro
    for filho in p.filhos:
        print(filho.nome)
    p.sobrenome = "Carmelita de Lisieux Mol"  # cria o atributo dinamicamente
    f.sobrenome = "Lisieux Leal e Mol"

    print(p.__dict__)
    print(f.__dict__)

    del p.sobrenome  # deleta o atributo
    print("Olhos: ", Pessoa.olhos)
    print("Olhos: ", p.olhos)
    print(Pessoa.metodo_estatico(), f.metodo_estatico())
    print(isinstance(p, Pessoa))
    print(isinstance(p, Mulher))
    print(isinstance(f, Pessoa))
    print(isinstance(f, Mulher))

