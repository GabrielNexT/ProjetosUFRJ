import random
import queue

class Grafo:
  def __init__(self, size):
    self.grafo = {}
    for i in range(size):
      self.grafo[i] = []

  def print(self):
    for i in self.grafo:
      print(i, self.grafo[i])

  def addEdge(self, fr, to):
    self.grafo[fr].append(to)

  def bfs(self, index):
    vis = [False] * len(self.grafo)
    q = queue.Queue()
    q.put(index)
    while not q.empty():
      u = q.get()
      if(vis[u]):
        continue
      else:
        vis[u] = True
      print(f"Visitando os vizinhos do {u}")
      for i in self.grafo[u]:
        q.put(i)      



size = 5

v = Grafo(size)
for i in range(size * 2):
  v.addEdge(random.randint(0, size - 1), random.randint(0, size - 1))
v.print()
print('-------')
v.bfs(1)