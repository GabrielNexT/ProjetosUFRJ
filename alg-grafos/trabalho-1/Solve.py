'''
  Gabriel Oliveira de Março - 118147655

  Algoritmo e grafos

  O algoritmo suporta vértices de tamanho até 1000.
  Caso queira colocar um valor maior, aumentar o MAXN abaixo.

  A complexidade do algoritmo é O(n^3)

  Para a entreda, é necessário que exista um arquivo chamado entrada.txt na raiz do arquivo.
  A saída será no stdout, usando o operador > do linux, é possível inserir em um arquivo.
'''

MAXN = 1000
graph = [set() for i in range(0, MAXN)]
vertexs = set()

def printGrafo():
  for i in range(0, len(graph)):
    if (len(graph[i]) > 0):
      print(i, '->', graph[i])

with open('entrada.txt', '+r') as file:
  for line in file:
    a = line.split()
    a.remove('=')
    a = [int(x) for x in a]
    vertexs.add(a[0])
    for i in range(1, len(a)):
      vertexs.add(a[i])
      graph[a[0]].add(a[i])
      graph[a[i]].add(a[0])

N = len(vertexs) + 1
pq = set()

for i in range(1, N):
  pq.add((0, i))

index = [[]] * N
inside = [[]] * N
ords = []

printGrafo()

while len(pq) > 0:
  pair = pq.pop()
  u = pair[1]
  index[u] = len(ords)
  ords.append(u)
  inside[u] = -1

  for v in graph[u]:
    if inside[v] == -1:
      continue
    remove_set = set()
    remove_set.add((0, v))
    pq = pq - remove_set
    inside[v] = 1
    pq.add((inside[v], v))

for u in ords:
  prev = -1
  for v in graph[u]:
    if index[v] < index[u] and index[v] > prev:
      prev = index[v]

  if prev == -1:
    continue

  z = ords[prev]

  for v in graph[u]:
    if index[v] < index[z] and not v in graph[z]:
      print("NO")
      exit(0)

print("YES")