import sys
from heapq import heappop, heappush 
class Node:
    def init(self, vertice, peso=0):
        self.vertice = vertice
        self.peso = peso
 
    def lt(self, other):
        return self.peso < other.peso
 
class Graph:
    def init(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (principio, destino, peso) in edges:
            self.adjList[principio].append((destino, peso))
 
 
def ruta(previo, i, ruta):
    if i >= 0:
        ruta(previo, previo[i], ruta)
        ruta.append(i)
        
def nombres_ruta(ruta):
    nombres=['Alderan','Alderan2','Endor','Endor2','Dagobah','Dagobah2','Hoth','Hoth2'
    'Tatooine','Tatooine2','Kamino','Kamino2','Naboo','Naboo2','Mustafar','Mustafar2',
    'Escarif','Escarif2','Bespin']
    nombre_ruta=[]
    for i in range(len(ruta)):
        numero = ruta[i]
        nombre = nombres[numero]
        nombre_ruta.append(nombre)
        print
 
def findShortestPaths(graph, principio, n):
 
    pq = []
    heappush(pq, Node(principio))
 
    distancia = [sys.maxsize] * n
    distancia[principio] = 0
 
    done = [False] * n
    done[source] = True
    previo = [-1] * n
    
    while pq:
        node = heappop(pq)      
        u = node.vertice        
 
        for (v, peso) in graph.adjList[u]:
            if not done[v] and (distancia[u] + peso) < distancia[v]:        
                distancia[v] = distancia[u] + peso
                previo[v] = u
                heappush(pq, Node(v, distancia[v]))

        done[u] = True
 
    ruta = []
    nombres_ruta = []
    nombres=['Alderan','Alderan2','Endor','Endor2','Dagobah','Dagobah2','Hoth','Hoth2'
    'Tatooine','Tatooine2','Kamino','Kamino2','Naboo','Naboo2','Mustafar','Mustafar2',
    'Escarif','Escarif2','Bespin']
    for i in range(n):
        if i != principio and distancia[i] != sys.maxsize:
            ruta(previo, i, ruta)
            for r in range(len(ruta)):
                num = ruta[r]
                name_c = nombres[num]
                nombres_ruta.append(name_c)
            print(f'Path ({nombres[source]} —> {nombres[i]}): Minimum cost = {distancia[i]}, Route = {nombres_ruta}')
            ruta.clear()
            nombres_ruta.clear()
 
 
if __name__=='main':

    edges = [(0, 1, 10), (0, 4, 3), (1, 2, 2), (1, 4, 4), (2, 3, 9), (3, 2, 7),
            (4, 1, 1), (4, 2, 8), (4, 3, 2),(1,8,0),(2,8,1),(1,9,1),(1,8,1),(1,8)]
    n=5

    graph = Graph(edges, n)
 
    for source in range(n):
        findShortestPaths(graph, principio, n)
