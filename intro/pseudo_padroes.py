import numpy as np 
from random import random

class Automatos:
	def __init__(self, matriz):
		self.matriz = np.array(matriz)
		self.symb = []
		self.p = []
	def deterministic(self, inter, s):
		self.symb = s
		i = 0
		for k in range(inter):
			r = random()
			a = 0
			for j in range(len(self.matriz)):
				a = a + self.matriz[i][j]
				if r < a:
					self.p.append(self.symb[i])
					i = j
					break
		return self.p
		
M = [[0.5,0.5,0,0],
	[0,0.1,0.9,0],
	[0,0,0.6,0.4],
	[0.7,0,0,0.3]
	] 
auto = Automatos(M)
padroes_fig2 = auto.deterministic(20, [0,1,2,3])
print(padroes_fig2)
print(len(padroes_fig2))