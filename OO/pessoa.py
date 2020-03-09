class Pessoa:
    def __init__(self, nome=None, idade=45):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f"Olá!!! {id(self)}"


if __name__ == "__main__":
    p = Pessoa('Christiane')
    print(Pessoa.cumprimentar(p))  # chamada do método
    print(p.cumprimentar())  # chamada do método
    print(p.nome)  # acesso ao parâmetro
    p.nome = "Christiane"  # atribuindo valor ao parâmetro
