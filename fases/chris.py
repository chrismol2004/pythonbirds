# -*- coding: utf-8 -*-
from os import path
import sys

project_dir = path.dirname(__file__)
project_dir = path.join('..')
sys.path.append(project_dir)

from atores import PassaroAmarelo, PassaroVermelho, Obstaculo, Porco
from fase import Fase
from placa_grafica_tkinter import rodar_fase

if __name__ == '__main__':
    fase = Fase(intervalo_de_colisao=20)


    deltax_gambi=100
    # Adicionar Pássaros Amarelos
    for i in range(50):
        fase.adicionar_passaro(PassaroAmarelo(30, 30))
    inicio = 200
    fim = 600
    # linhas verticais
    for i in range(100, 300, 50):
        fase.adicionar_porco(Porco(fim - deltax_gambi, i))
        fase.adicionar_porco(Porco(inicio - deltax_gambi, i))

        fase.adicionar_porco(Porco(i*2, fim-deltax_gambi*3))
        fase.adicionar_porco(Porco(i*2, inicio-deltax_gambi))

    x0 = 200-deltax_gambi
    # losango
    meio = 200
    n = 5
    delta_x = 40
    delta_y = 15
    for i in range(1, n):
        fase.adicionar_porco(Porco(x0 + delta_x * i, meio + delta_y * i))
        fase.adicionar_porco(Porco(x0 + delta_x * i, meio - delta_y * i))
        fase.adicionar_porco(Porco(x0 + (n + i - 1) * delta_x, meio + (n - i) * delta_y))
        fase.adicionar_porco(Porco(x0 + (n + i - 1) * delta_x, meio + (i - n) * delta_y))

    rodar_fase(fase)