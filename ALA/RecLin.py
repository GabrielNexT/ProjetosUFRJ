# -*- coding: utf-8 -*-
#coding: utf-8

import numpy
import math

mod = int(1e9+7)

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
  return fib[1]

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
      ans[i][j] = (i == j)
  
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

  return M[0][0] + M[0][1]

maxN = 15

# print(defaultFib(maxN))
# print(linearFib(maxN))
# print(linearFibUsingAL(maxN))

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

def buildBase(c):
  base = [[0 for x in range(len(c))] for y in range(len(c))]
  for i in range (0, len(c)):
    base[0][i] = c[i]
  for i in range (1, len(c)):
    for j in range (0, len(c)):
      base[i][j] = int(i-1 == j)
  return base

def seq(b, c, n):
  if(n <= len(b)):
    return b[n-1]

  M = buildBase(c)
  M = fastExponentiation(M, n-1)
  print(b)
  print(M)
  ans = 0
  for i in range(0, len(M)):
    ans += (M[0][i] * b[len(b)-i-1]) % mod  
  return ans

print(seq([1, 2, 3], [4, 5, 6], 6))
