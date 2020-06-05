import functools
import numpy as np
import math
import matplotlib.pyplot as plt

class Automatos:
    def __init__(self, M):
        self.matriz = np.array(M)
        self.symb = []
        self.padroes = []
    def symbols(self,S):
        self.symb = S
    def deterministic(self, inter):
        k = 0
        for i in range(inter):
            r = np.random.random_sample()
            a = 0
            for j in range(len(self.matriz)):
                a = a + self.matriz[k][j]
                if r < a:
                    self.padroes.append(self.symb[k])
                    k = j
                    break
        return self.padroes
    
M = [[0.5,0.5,0,0],
    [0,0.1,0.9,0],
    [0,0,0.6,0.4],
    [0.7,0,0,0.3]
    ] 

def euclidean_distance(row1,row2):
  distance = 0.0
  for i in range(len(row1)-1):
    distance += (row1[i]-row2[i])**2
  return math.sqrt(distance)

def get_neighbors(train, test_row, num_neighbors):
  distance = list()
  for i in range(len(train)):
    dist = euclidean_distance(test_row, train[i])
    distance.append((train[i], dist))
  distance.sort(key=lambda tup: tup[1])
  neighbors = list()
  for i in range(num_neighbors):
    neighbors.append(distance[i][0])
  return neighbors

auto1 = Automatos(M)
auto1.symbols([0,1,2,3])
padroes1 = auto1.deterministic(10)
auto2 = Automatos(M)
auto2.symbols([0,1,2,3])
padroes2 = auto2.deterministic(10)

neighbors = get_neighbors(padroes1, padroes2, 3)
for neighbor in neighbors:
  print(neighbor)