import numpy
import math

def defaultFib (n):
  if n == 1 or n == 2:
    return 1
  else:
    return defaultFib(n-1)+defaultFib(n-2)

def linearFib (n):
  fib = [1, 1]
  for i in xrange(2, n):
    fib.append(fib[1] + fib[0])
    fib.pop(0)
  return fib[1]

def prodMatrix (A, B):
  n = len(A)
  mul = [[0 for x in range(n)] for y in range(n)]
  for i in range(0, n):
    for j in range(n):
      mul[i][j] = 0
      for k in range(n):
        mul[i][j] += A[i][k] * B[k][j]

  for i in range(n):
    for j in range(n):
      A[i][j] = mul[i][j]
  return A

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
  if n == 1 or n == 2:
    return 1
  M = numpy.array([[1, 1], [1, 0]])
  M = fastExponentiation(M, n-2)

  return M[0][0] + M[0][1]

maxN = 15

# print(defaultFib(maxN))
# print(linearFib(maxN))
print(linearFibUsingAL(maxN))