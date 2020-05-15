import numpy as np 

def main():
	padroes_fig1d = Padroes()
	padroes_fig1d.matriz_aleatoria()
	padroes_fig1d.symbols_padrao()
	padroes_fig1d.next_step(10)


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
				else: continue
		print(self.padroes_gerados)		
		
if __name__ == '__main__':
	main()
