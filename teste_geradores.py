# geradores_teste.py
""" Rotina para testar o módulo geradores
"""

from geradores import SquareWave
import numpy as np
import matplotlib.pyplot as plt

# parâmetros do gerador de onda quadrada
ciclo_de_trabalho = 0.6  # o ciclo de trabalho dever ser um valor entre 0 e 1
tempo_total = 2 # em segundos
frequencia_de_amostragem = 1e4 # em Hertz
frequencia_fundamental = 1 # em Hertz

# Definição de um gerador de onda quadrada com os parâmetros acima definidos
gerador_onda_quadrada = SquareWave(ciclo_de_trabalho, tempo_total, frequencia_de_amostragem, frequencia_fundamental)

# Inspeção do gerador_onda_quadrada
print('Formalmente o gerador é um objeto da classe SquareWave. A seguir listaremos os atributos dessa classe:')
print('Ciclo de trabalho: ', gerador_onda_quadrada.duty_cycle)
print('Tempo total: ', gerador_onda_quadrada.total_time)
print('Frequênca de amostragem: ', gerador_onda_quadrada.sampling_frequency)
print('Frequência fundamental: ', gerador_onda_quadrada.frequency)
print('Período: ', gerador_onda_quadrada.period)
print('\nSão ainda atributos um vetor tempo e o sinal propriamente dito, que serão exibidos em um gráfico')

plt.figure()
plt.plot(gerador_onda_quadrada.time, gerador_onda_quadrada.signal,'b')
plt.grid(True)
plt.title('Sinal do gerador de onda quadrada')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.show()

