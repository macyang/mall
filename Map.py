from Vertex import Vertex
from Graph import Graph

class Map:
    def __init__(self):
      g = Graph()

      g.addVertex(0, 1.0, 2.0)
      g.addVertex(1, 1.0, 3.0)
      g.addVertex(2, 2.0, 1.0)
      g.addVertex(3, 2.0, 2.0)
      g.addVertex(4, 2.0, 3.0)
      g.addVertex(5, 2.0, 4.0)
      g.addVertex(6, 3.0, 1.0)
      g.addVertex(7, 3.0, 2.0)
      g.addVertex(8, 3.0, 3.0)
      g.addVertex(9, 3.0, 4.0)
      g.addVertex(10, 4.0, 1.0)
      g.addVertex(11, 4.0, 2.0)
      g.addVertex(12, 4.0, 3.0)
      g.addVertex(13, 4.0, 4.0)
      g.addVertex(14, 5.0, 2.0)
      g.addVertex(15, 5.0, 3.0)

      g.addEdge(0, 0, 0.5)
      g.addEdge(0, 3, 0.5)
      g.addEdge(1, 1, 0.5)
      g.addEdge(1, 4, 0.5)
      g.addEdge(2, 3, 1.0)
      g.addEdge(3, 0, 0.3)
      g.addEdge(3, 2, 0.1)
      g.addEdge(3, 4, 0.3)
      g.addEdge(3, 7, 0.3)
      g.addEdge(4, 1, 0.2)
      g.addEdge(4, 3, 0.2)
      g.addEdge(4, 5, 0.2)
      g.addEdge(4, 8, 0.4)
      g.addEdge(5, 4, 0.5)
      g.addEdge(5, 5, 0.5)
      g.addEdge(6, 6, 0.5)
      g.addEdge(6, 7, 0.5)
      g.addEdge(7, 3, 0.2)
      g.addEdge(7, 6, 0.3)
      g.addEdge(7, 11, 0.5)
      g.addEdge(8, 4, 0.2)
      g.addEdge(8, 9, 0.4)
      g.addEdge(8, 12, 0.4)
      g.addEdge(9, 8, 0.5)
      g.addEdge(9, 9, 0.5)
      g.addEdge(10, 10, 0.5)
      g.addEdge(10, 11, 0.5)
      g.addEdge(11, 7, 0.2)
      g.addEdge(11, 10, 0.2)
      g.addEdge(11, 12, 0.2)
      g.addEdge(11, 14, 0.4)
      g.addEdge(12, 8, 0.2)
      g.addEdge(12, 11, 0.4)
      g.addEdge(12, 13, 0.6)
      g.addEdge(13, 12, 0.5)
      g.addEdge(13, 13, 0.5)
      g.addEdge(14, 11, 0.4)
      g.addEdge(14, 14, 0.2)
      g.addEdge(14, 15, 0.4)
      g.addEdge(15, 14, 0.5)
      g.addEdge(15, 15, 0.5)

      self.graph = g

    def getGraph(self):
      return self.graph

    def __str__(self):
      for v in self.graph:
	for w in v.getConnections():
	  print("( %s , %s )" % (v.getId(), w.getId()))
      return ''
