import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import norm
import seaborn as sns
import time

inicio = time.time()

class Padroes:
	def __init__(self):
		self.matriz = []
		self.symbols = []
		self.padroes_gerados = []
	def matriz_aleatoria(self):
		self.matriz = [[0.2,0.8],[0.2,0.8]]
		self.matriz = np.array(self.matriz)
	def symbols_padrao(self):
		self.symbols = [0,1] 
	def next_step(self, inter):
		k = 0
		for i in range(inter):
			p = 0
			r = np.random.random_sample()
			for j in range(len(self.matriz)):
				p = p + self.matriz[k][j]
				if r < p:
					self.padroes_gerados.append(self.symbols[k])
					k = j
					break
		return (self.padroes_gerados)	

padroes_fig1d = Padroes()
padroes_fig1d.matriz_aleatoria()
padroes_fig1d.symbols_padrao()
#padrao = padroes_fig1d.next_step(10)


def freq(automato, symbol):
    automato = np.array(automato)
    counter = 0
    for i in automato: 
        if i==symbol: 
            counter +=1
    return counter/automato.size

#print(freq(padrao, 1))
f_a = []
for i in range(200,2000,200):
	#for j in range(200):
	f_a.append(freq(padroes_fig1d.next_step(i),1))
	sns.distplot(f_a, color="dodgerblue", hist = False, kde = True)

#print(f_a)
plt.xlim(0,1)
plt.xlabel("Frequência de \"1\"")
plt.ylabel("Densidade de ocorrência")
plt.show()

fim = time.time()
print(fim-inicio)