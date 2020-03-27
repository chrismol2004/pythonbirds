class Motor:
    def __init__(self, ):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade +=1

    def frear(self):
        self.velocidade -= 1
        self.velocidade = max(0, self.velocidade)
)



class Direcao:
    rotacao_d = {'NORTE': 'LESTE', 'LESTE': 'SUL', 'SUL': 'OESTE', 'OESTE': 'NORTE' }
    rotacao_e = {'NORTE': 'OESTE', 'OESTE': 'SUL', 'SUL': 'LESTE', 'LESTE': 'NORTE' }

    def __init__(self):
        self.valor = 'NORTE'

    def girar_a_direita(self):
        self.valor = rotacao_d[self.valor]

    def girar_a_esquerda(self):
        self.valor = rotacao_e[self.valor]


class Carro:
    def __init__(self, direcao, motor):
        self.motor = motor
        self.direcao = direcao

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor
