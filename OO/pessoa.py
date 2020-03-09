class Pessoa:
    def __init__(self, *filhos, nome=None, idade=45 ):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f"Olá!!! {id(self)}"


if __name__ == "__main__":
    f = Pessoa(nome='Christiane')
    p = Pessoa(f, nome='Theresinha')
    print(Pessoa.cumprimentar(p))  # chamada do método
    print(p.cumprimentar())  # chamada do método
    print(p.nome)  # acesso ao parâmetro
    for filho in p.filhos:
    print(filho.nome)