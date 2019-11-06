# -*- coding: utf-8 -*-
#coding: utf-8
from PIL import Image
import numpy as np
import imageio
import matplotlib.pyplot as plt
import os

# Variáveis globais
src = os.listdir('src')
database = [[] for y in range(150*150)]

# Funções auxiliares

def matrixToArray(matrix):
  ans = []
  for i in range(len(matrix)):
    for j in range(len(matrix)):
      ans.append(matrix[i][j])
  return ans

def insertOnDatabase(vector):
  for i in range(len(vector)):
    database[i].append(vector[i])

def push(matrix):
  vector = matrixToArray(matrix)
  insertOnDatabase(vector)

def findAvarage():
  avarage = []
  for x in range (len(database)):
    sum = 0 
    for y in range (33):
      sum += database[x][y]
    avarage.append(int(sum/33))
  return avarage

# Main
for i in src:
  img = imageio.imread('src/' + i)
  push(img)

print(len(database))
print(database[0])
print('Coluna Media:')
print(findAvarage())