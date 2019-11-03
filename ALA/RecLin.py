# -*- coding: utf-8 -*-
#coding: utf-8

import numpy
import math
import timeit

mod = int(1e9)

# Fib padrão feito de várias formais distinstas.

def defaultFib (n):
  if n == 0 or n == 1:
    return 1
  else:
    return defaultFib(n-1) + defaultFib(n-2)

def linearFib (n):
  fib = [1, 1]
  for i in xrange(2, n+1):
    fib.append(fib[1] % mod + fib[0] % mod)
    fib.pop(0)
  return fib[1] % mod

def prodMatrix (A, B):
  n = len(A)
  mul = [[0 for x in range(n)] for y in range(n)]
  for i in range(0, n):
    for j in range(n):
      mul[i][j] = 0
      for k in range(n):
        mul[i][j] += (A[i][k] * B[k][j]) % mod
  return mul

def fastExponentiation (A, pow):
  n = len(A)
  ans = [[0 for x in range(n)] for y in range(n)]
  for i in range(n):
    for j in range(n):
      ans[i][j] = int(i == j)
  
  while(pow):
    if (pow & 1): 
      ans = prodMatrix(ans, A)
    A = prodMatrix(A, A)
    pow >>= 1

  return ans

def linearFibUsingAL (n):
  if n == 0 or n == 1:
    return 1
  M = [[1, 1], [1, 0]]
  M = fastExponentiation(M, n-1)

  return (M[0][0] + M[0][1]) % mod

maxN = int(1e8)

def printTime(function, maxN):
  # label = function +'(' + str(maxN) + ')', 'from __main__ import'+ ' ' + function
  print(timeit.Timer( function +'(' + str(maxN) + ')', 'from __main__ import'+ ' ' + function ).repeat(1,1))
  return

# printTime('defaultFib', maxN)
# print(defaultFib(maxN))
printTime('linearFib', maxN)
print(linearFib(maxN))
printTime('linearFibUsingAL', maxN)
print(linearFibUsingAL(maxN))

# # Tribonacci
def defaultTri (n):
  if n == 0:
    return 0
  elif n == 2 or n == 1:
    return 1
  else:
    return defaultTri(n-1) + defaultTri(n-2) + defaultTri(n-3)

def linearTri (n):
  fib = [0, 1, 1]
  if n <= 2:
    return fib[n]
  for i in xrange(3, n+1):
    fib.append(fib[1] % mod + fib[0] % mod + fib[2] % mod)
    fib.pop(0)
  return fib[2]

def linearTriUsingALA (n):
  if n == 0 or n == 1:
    return 1
  if n == 2:
    return 2
  M = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
  M = fastExponentiation(M, n-2)
  return M[0][0] + M[0][1] + 0*M[0][2]

# print(defaultTri(maxN))
# print(linearTri(maxN))
# print(linearTriUsingALA(maxN))

# SEQ - Recursive Sequence

def buildBase(mat):
  base = [[0 for x in range(len(mat))] for y in range(len(mat))]
  for i in range (0, len(mat)):
    base[0][i] = mat[i]
  for i in range (1, len(mat)):
    for j in range (0, len(mat)):
      base[i][j] = int(i-1 == j)
  return base

# Função que resolve a questão SEQ. USAR MOD 1e9 
def seq(b, c, n):
  M = buildBase(c)
  M = fastExponentiation(M, n-len(M))
  ans = 0
  for i in range(0, len(M)):
    ans += (M[len(M)-1][len(M)-i-1] * b[i]) % mod 
  return ans % mod

print(seq([1, 2, 3], [4, 5, 6], 6))



# print(seq([1, 2, 3], [4, 5, 6], 6))
