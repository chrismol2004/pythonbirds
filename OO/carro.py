"""Criar uma classe que possui dois atributos compostos por outras duas classes:
1) Motor: terá a responsabilidade de controlar a velocidade: oferecendo:
   - o atributo velocidade:
   - Metodo acelerar: acrescenta uma unidade a velocidade
   - Metodo frear: decrementa duas unidades a velocidade

2) Direção: terá a responsabilidade de controlar a direção, oferecendo os atributos:
   - valor da direção: Norte, Sul, leste e Oeste.
   - Método girar a direita                             N
   - Método girar a esquerda.                        O     L
                                                        S
    Exemplo:
    # testando motor
    >> motor = Motor()
    >> motor.velocidade
    0
    >> motor.acelerar()
    >> motor.velocidade
    1
    >> motor.acelerar()
    >> motor.velocidade
    2
    >> motor.acelerar()
    >> motor.velocidade
    3
    >> motor.frear()
    >> motor.velocidade
    0
    # testando direção
    >> direcao = Direçao()
    >> direcão.valor
    'Norte'
    >> direcao.girar_direita()
    >> direcão.valor
    'Leste'
    >> direcao.girar_direita()
    >> direcão.valor
    'Sul'
    >> direcao.girar_direita()
    >> direcão.valor
    'Oeste'
    >> direcao.girar_esquerda()
    >> direcão.valor
    'Sul'
    >> direcao.girar_esquerda()
    >> direcão.valor
    'Leste'
    >> direcao.girar_esquerda()
    >> direcão.valor
    'Norte'

    >> direcao.girar_direita()
    >> direcão.valor
    'Oeste'

    >> carro = Carro()
"""


class Direcao:
    direcoes = {1: 'Norte', 2: 'Leste', 3: 'Sul', 4: 'Oeste'}

    def __init__(self, direcao=1):
        self.direcao = direcao
        self.valor = self.direcoes[direcao]

    def gira_direita(self):
        self.direcao += 1
        if self.direcao > 4:
            self.direcao = 1
        self.valor = self.direcoes[self.direcao]

    def gira_esquerda(self):
        self.direcao = self.direcao - 1
        if self.direcao < 1:
            self.direcao = 4
        self.valor = self.direcoes[self.direcao]


class Motor:
    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def frear(self):
        if self.velocidade:
            self.velocidade -= 2
        return self.velocidade

    def acelerar(self):
        self.velocidade += 1
        return self.velocidade


class Carro:
    def __init__(self, direcao, motor):
        self.motor = motor
        self.direcao = direcao

    def caracteristicas(self):
        return f'O Carro tem velocidade de {self.motor.velocidade} e está na direçãõ {self.direcao.valor}'

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()


if __name__ == "__main__":
    motor1 = Motor()
    print(motor1.velocidade)
    Motor.acelerar(motor1)
    print(motor1.velocidade)
    Motor.acelerar(motor1)
    print(motor1.velocidade)
    Motor.acelerar(motor1)
    print(motor1.velocidade)

    direcao1 = Direcao()
    print(direcao1.valor)
    Direcao.gira_direita(direcao1)
    print(direcao1.valor)
    Direcao.gira_direita(direcao1)
    print(direcao1.valor)
    Direcao.gira_direita(direcao1)
    print(direcao1.valor)

    carro1 = Carro(direcao1, motor1)
