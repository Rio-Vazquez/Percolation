import random



class Vertex:
	# `index` is a unique integer identifier, `color` is an integer in [-1, 0, 1].
	# Silver vertices have color=0, and teal vertices have color=1.
	# Unmarked vertices have color=-1.
	def __init__(self, index, color=-1):
		self.index = index
		self.color = color

class Edge:
	# `a` and `b` are Vertex objects corresponding to the endpoints of this edge.
	def __init__(self, a, b):
		self.a = a
		self.b = b

class Graph:
	# `vertices` and `edges` are iterables of Vertex and Edge objects respectively
	# Internally, we store these as set()s on the graph class.
	def __init__(self, vertices, edges):
		self.V = set(vertices)
		self.E = set(edges)

def Neighbor(self, v):
		answers = []
		x = 0
		while x<len(self.E):
			newdata = list(self.E)[x]
			if newdata.a == v:
				answers.append(newdata.a.color)
			elif newdata.b == v:
				answers.append(newdata.b.color)
			x = x + 1
		return answers


class PercolationPlayer:
	
	

	# `graph` is an instance of a Graph, `player` is an integer (0 or 1).
	# Should return a vertex `v` from graph.V where v.color == -1
	def ChooseVertexToColor(graph, player):
		v1 = list(graph.V)
		v4 = list(graph.E)
		x=0
		for x in range(0, len(v1)):
			if v1[x].color == -1:
				for y in range(0, len(v4)):
					if v4[y].a == v1[x] and v4[y].b.color == player or -1:
						return v1[x]
					elif v4[y].b == v1[x] and v4[y].a.color == player or -1:
						return v1[x]
	

		return (random.choice(v1))




# `graph` is an instance of a Graph, `player` is an integer (0 or 1).
# Should return a vertex `v` from graph.V where v.color == player
	def ChooseVertexToRemove(graph, player):
		v1 = list(graph.V)
		v4 = list(graph.E)
		x=0
		for x in range(0, len(v1)):
			if v1[x].color == player:
				for y in range(0, len(v4)):
					if v4[y].a == v1[x] and v4[y].b.color == (1-player):
						return v1[x]
					elif v4[y].b == v1[x] and v4[y].a.color == (1-player):
						return v1[x]
	

		return (random.choice(v1))


def main():
	   pass

if __name__ == "__main__":
    main()



