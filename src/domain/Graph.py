from random import randrange
from copy import deepcopy

from exceptions import VertexError, EdgeError


class Graph:
    """
    A class representing a Directed Graph.
    """

    def __init__(self, vertex_count: int = 0, edge_count: int = 0) -> None:
        self.__vertices = set()
        self.__neighbours = dict()
        self.__transpose = dict()
        self.__costs = dict()
        self.__durations = dict()

        for vertex in range(vertex_count):
            self.add_vertex(vertex)

        for _ in range(edge_count):
            vertex1 = randrange(vertex_count)
            vertex2 = randrange(vertex_count)

            while self.is_edge(vertex1, vertex2):
                vertex1 = randrange(vertex_count)
                vertex2 = randrange(vertex_count)

            # Edge cost is random
            self.add_edge(vertex1, vertex2, randrange(1000))

    @property
    def vertices(self) -> set:
        """
        :return: the set of vertices
        """
        return self.__vertices

    @property
    def neighbours(self) -> dict:
        """
        :return: the dictionary of neighbours
        """
        return self.__neighbours

    @property
    def transpose(self) -> dict:
        """
        :return: the dictionary of the transposed graph
        """
        return self.__transpose

    @property
    def costs(self) -> dict:
        """
        :return: the dictionary of edge costs
        """
        return self.__costs

    @property
    def durations(self) -> dict:
        """
        :return: the dictionary of activity durations
        """
        return self.__durations

    def vertices_iterator(self) -> iter:
        """
        Returns an iterator to the set of vertices.
        """
        for vertex in self.vertices:
            yield vertex

    def neighbours_iterator(self, vertex: int) -> iter:
        """
        Returns an iterator to the set of (outbound) neighbours of a vertex.
        """
        if not self.is_vertex(vertex):
            raise VertexError("ERROR: Invalid vertex.")

        for neighbour in self.neighbours[vertex]:
            yield neighbour

    def transpose_iterator(self, vertex: int) -> iter:
        """
        Returns an iterator to the set of (inbound) neighbours of a vertex.
        """
        if not self.is_vertex(vertex):
            raise VertexError("ERROR: Invalid vertex.")

        for neighbour in self.transpose[vertex]:
            yield neighbour

    def edges_iterator(self) -> iter:
        """
        Returns an iterator to the set of edges.
        """
        for key, value in self.costs.items():
            yield key[0], key[1], value

    def is_vertex(self, vertex: int) -> bool:
        """
        Returns True if vertex belongs to the graph.
        """
        return vertex in self.vertices

    def is_edge(self, vertex1: int, vertex2: int) -> bool:
        """
        Returns True if the edge from vertex1 to vertex2 belongs to the graph.
        """
        return vertex1 in self.neighbours and vertex2 in self.neighbours[vertex1]

    def vertex_count(self) -> int:
        """
        Returns the number of vertices in the graph.
        """
        return len(self.vertices)

    def edge_count(self) -> int:
        """
        Returns the number of edges in the graph.
        """
        return len(self.costs)

    def in_degree(self, vertex: int) -> int:
        """
        Returns the number of edges with the endpoint vertex.
        """
        if vertex not in self.transpose:
            raise VertexError("ERROR: Vertex does not exist.")

        return len(self.transpose[vertex])

    def out_degree(self, vertex: int) -> int:
        """
        Returns the number of edges with the start point vertex.
        """
        if vertex not in self.neighbours:
            raise VertexError("ERROR: Vertex does not exist.")

        return len(self.neighbours[vertex])

    def get_edge_cost(self, vertex1: int, vertex2: int) -> int:
        """
        Returns the cost of an edge if it exists.
        """
        if (vertex1, vertex2) not in self.costs:
            raise EdgeError("ERROR: Edge does not exist.")

        return self.costs[(vertex1, vertex2)]

    def set_edge_cost(self, vertex1: int, vertex2: int, new_cost: int) -> None:
        """
        Sets the cost of an edge in the graph if it exists.
        """
        if (vertex1, vertex2) not in self.costs:
            raise EdgeError("ERROR: Edge does not exist.")

        self.costs[(vertex1, vertex2)] = new_cost

    def add_vertex(self, vertex: int) -> None:
        """
        Adds a vertex to the graph.
        """
        if self.is_vertex(vertex):
            raise VertexError("ERROR: Vertex already exists.")

        self.vertices.add(vertex)
        self.neighbours[vertex] = set()
        self.transpose[vertex] = set()

    def add_edge(self, vertex1: int, vertex2: int, edge_cost: int = 0) -> None:
        """
        Adds an edge to the graph.
        """
        if self.is_edge(vertex1, vertex2):
            raise EdgeError("ERROR: Edge already exists")

        if not self.is_vertex(vertex1) or not self.is_vertex(vertex2):
            raise EdgeError("ERROR: Vertices on edge do not exist.")

        self.neighbours[vertex1].add(vertex2)
        self.transpose[vertex2].add(vertex1)
        self.costs[(vertex1, vertex2)] = edge_cost

    def remove_edge(self, vertex1: int, vertex2: int) -> None:
        """
        Removes an edge from the graph.
        """
        if not self.is_edge(vertex1, vertex2):
            raise EdgeError("ERROR: Edge does not exist.")

        del self.costs[(vertex1, vertex2)]
        self.neighbours[vertex1].remove(vertex2)
        self.transpose[vertex2].remove(vertex1)

    def remove_vertex(self, vertex: int) -> None:
        """
        Removes a vertex from the graph.
        """
        if not self.is_vertex(vertex):
            raise VertexError("ERROR: Vertex doesn't exist.")

        to_remove = list()
        for node in self.neighbours[vertex]:
            to_remove.append(node)
        for node in to_remove:
            self.remove_edge(vertex, node)

        to_remove = list()
        for node in self.transpose[vertex]:
            to_remove.append(node)
        for node in to_remove:
            self.remove_edge(node, vertex)

        del self.neighbours[vertex]
        del self.transpose[vertex]

        self.vertices.remove(vertex)

    def copy(self) -> "Graph":
        """
        Returns a deep copy of the graph instance.
        """
        return deepcopy(self)
