import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import numpy as np 
import random
import math

def main():
	pca_preparo = PCA()
	pca_preparo.aleatorios(500)
	pca_preparo.circulo()
	pca_preparo.alongamento()
	pca_preparo.rotacao()
	pca_preparo.plot()

class PCA:
	def __init__(self):
		self.aleatorios_x = []
		self.aleatorios_y = []
		self.aleatorios_z = []
		self.circulo_x = []
		self.circulo_y = []
		self.circulo_z = []
		self.circulo_y_alongado = []
		self.circulo_z_alongado = []
		self.rotacao_ = []
	def aleatorios(self,interacoes):
		for i in range(interacoes):
			k = random.uniform(-1,1)
			h = random.uniform(-1,1)
			p = random.uniform(-1,1)
			self.aleatorios_x.append(k)
			self.aleatorios_y.append(h)
			self.aleatorios_z.append(p)
	def circulo(self):
		for i in range(len(self.aleatorios_x)):
			k = math.sqrt((self.aleatorios_y[i])**2 + (self.aleatorios_x[i])**2 + (self.aleatorios_z[i])**2)
			if k <= 1:
				self.circulo_x.append(self.aleatorios_x[i])
				self.circulo_y.append(self.aleatorios_y[i])
				self.circulo_z.append(self.aleatorios_z[i])
			else:
				continue
	def alongamento(self):
		for i in range(len(self.circulo_y)):
			self.circulo_y_alongado.append(0)
			self.circulo_z_alongado.append(0)
		for i in range(len(self.circulo_y)):
			self.circulo_y_alongado[i] = 0.2*self.circulo_y[i]
			self.circulo_z_alongado[i] = 0.2*self.circulo_z[i]
	def rotacao(self):
		k = np.radians(30)
		rot = [[np.cos(k),np.sin(k)],[np.sin(k),np.cos(k)]]
		self.rotacao_ = np.dot(rot,[self.circulo_x,self.circulo_y_alongado])
	def plot(self):
		fig = plt.figure()
		ax = fig.add_subplot(111,projection = '3d')
		ax.scatter(self.circulo_x,self.circulo_y,self.circulo_z,marker = 'o')
		plt.show()

if __name__ == '__main__':
	main()