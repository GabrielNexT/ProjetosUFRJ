from PIL import Image
import numpy as np
import imageio
import matplotlib.pyplot as plt
import os

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


src = os.listdir('src')

database = [[] for y in range(150*150)]

for i in src:
  img = imageio.imread('src/' + i)
  push(img)

print(database[0])