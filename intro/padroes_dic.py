import numpy as np 

def main():
	padroes_fig1d = Padroes()
	padroes_fig1d.matriz_aleatoria()
	padroes_fig1d.symbols_padrao()
	padroes_fig1d.next_step(7)


class Padroes:
	def __init__(self):
		self.dic_matriz = {'fig_6a':'' ,'fig_6b':'' ,'fig_6c':''}
		self.padroes_fig6a = []
		self.padroes_fig6b = []
		self.padroes_fig6c = []
		self.padroes = {'fig_6a':'' ,'fig_6b':'' ,'fig_6c':''}
		self.symbols = []
	def matriz_aleatoria(self):
		self.dic_matriz['fig_6a'] = np.array([[0.9,0.1],[0.9,0.1]])
		self.dic_matriz['fig_6b'] = np.array([[0.2,0.8],[0.2,0.8]])
		self.dic_matriz['fig_6c'] = np.array([[0.5,0.5],[0.5,0.5]])
	def symbols_padrao(self):
		self.symbols = [0,1] 
	def next_step(self, inter):
		for key in self.dic_matriz.keys():
			for value in self.dic_matriz.values():	
				k = 0
				for i in range(inter):
					p = 0
					r = np.random.random_sample()
					for j in range(len(value)):
						p = p + value[k][j]
						if r < p:
							if key == 'fig_6a':
								self.padroes_fig6a.append(self.symbols[k])
								k = j
								break
							elif key == 'fig_6b':
								self.padroes_fig6b.append(self.symbols[k])
								k = j
								break
							elif key == 'fig_6c':
								self.padroes_fig6c.append(self.symbols[k])
								k = j
								break
						#self.padroes_fig6a.append(self.symbols[k])
						#k = j
						#break
						else: continue
		print(len(self.padroes_fig6a))
		#print(self.padroes_fig6b)
		#print(self.padroes_fig6c)
	#def padroes_dic(self):		
		
if __name__ == '__main__':
	main()
