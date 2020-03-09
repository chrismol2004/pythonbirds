class Pessoa:
    def cumprimentar(self):
        return f"Olá!!! {id(self)}"

if __name__ == "__name__":
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())