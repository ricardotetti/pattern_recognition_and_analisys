import numpy as np 
from random import random

class Automatos:
	def __init__(self, matriz, symbols):
		self.matriz = np.array(matriz)
		self.symb = symbols
	def deterministic(self, inter):
		p = []
		i = 0
		for k in range(inter):
			r = random()
			a = 0
			for j in range(len(self.matriz)):
				a = a + self.matriz[i][j]
				if r < a:
					p.append(self.symb[i])
					i = j
					break
		return p
M = [[0.5,0.5,0,0],
	[0,0.1,0.9,0],
	[0,0,0.6,0.4],
	[0.7,0,0,0.3]
	] 
auto = Automatos(M, [0,1,2,3])
padroes_fig2 = auto.deterministic(20)
print(padroes_fig2)
print(len(padroes_fig2))