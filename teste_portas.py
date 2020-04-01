# teste_portas.py
""" Teste do módulo de portas lógicas"""

from portas import AndGate 
from geradores import SquareWave
import numpy as np
import matplotlib.pyplot as plt

# parâmetros do gerador de onda quadrada
ciclo_de_trabalho = 0.7  # o ciclo de trabalho dever ser um valor entre 0 e 1
tempo_total = 10e-9 # em segundos
frequencia_de_amostragem = 1e12 # em Hertz
frequencia_fundamental = 0.2e9 # em Hertz

# Definição de um gerador de onda quadrada com os parâmetros acima definidos
gerador_onda_quadrada = SquareWave(ciclo_de_trabalho, tempo_total, frequencia_de_amostragem, frequencia_fundamental)

tempo = gerador_onda_quadrada.time
sinal01 = gerador_onda_quadrada.signal
sinal02 = np.roll(sinal01, 1500)

# Definição de uma porta do tipo AND (sem atraso) e sua saída
atraso = 0 # sem atraso 
porta_and_a = AndGate(atraso)
porta_and_a.go(input_a = sinal01, input_b = sinal02, sam_period = 1/gerador_onda_quadrada.sampling_frequency)
saida_a = porta_and_a.output

# Definição de uma porta do tipo AND (atraso de  2 ns) e sua saída
atraso = 2 # atraso de dois nanossegundos
porta_and_b = AndGate(atraso)
porta_and_b.go(input_a = sinal01, input_b = sinal02, sam_period = 1/gerador_onda_quadrada.sampling_frequency)
saida_b = porta_and_b.output

plt.subplot(411)
plt.title('Teste da porta AND')
plt.plot(tempo, sinal01, 'r')
plt.ylabel('Entrada A')
plt.grid(True)
plt.subplot(412)
plt.plot(tempo, sinal02,'b')
plt.ylabel('Entrada B')
plt.grid(True)
plt.subplot(413)
plt.plot(tempo, saida_a,'k')
plt.ylabel('Saída A')
plt.grid(True)
plt.subplot(414)
plt.plot(tempo, saida_b,'k')
plt.ylabel('Saída B')
plt.grid(True)
plt.xlabel('Tempo (s)')
plt.show()

