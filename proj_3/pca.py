import matplotlib.pyplot as plt 
import numpy as np 
import random
import math

def main():
	pca_preparo = PCA()
	pca_preparo.aleatorios(200)
	pca_preparo.circulo()
	pca_preparo.alongamento()
	pca_preparo.rotacao()
	pca_preparo.plot()

class PCA:
	def __init__(self):
		self.aleatorios_x = []
		self.aleatorios_y = []
		self.circulo_x = []
		self.circulo_y = []
	def aleatorios(self,interacoes):
		for i in range(interacoes):
			k = random.uniform(-1,1)
			h = random.uniform(-1,1)
			self.aleatorios_x.append(k)
			self.aleatorios_y.append(h)
	def circulo(self):
		for i in range(len(self.aleatorios_x)):
			k = math.sqrt((self.aleatorios_y[i])**2 + (self.aleatorios_x[i])**2)
			if k <= 1:
				self.circulo_x.append(self.aleatorios_x[i])
				self.circulo_y.append(self.aleatorios_y[i])
			else:
				continue
	def alongamento(self):
		for i in range(len(self.circulo_y)):
			self.circulo_y[i] = 0.2*self.circulo_y[i]
	def rotacao(self):
		for i in range(len(self.circulo_x)):
			k = math.radians(30)
			self.circulo_x[i] = math.cos(k)*math.sin(k)*self.circulo_x[i]
			self.circulo_y[i] = math.sin(k)*math.cos(k)*self.circulo_y[i]
	def plot(self):
		plt.title("PCA")
		plt.xlabel("x")
		plt.ylabel("y")
		plt.xlim(-1,1)
		plt.ylim(-1,1)
		plt.scatter(self.circulo_x,self.circulo_y, s = 2)
		plt.show()


if __name__ == '__main__':
	main()