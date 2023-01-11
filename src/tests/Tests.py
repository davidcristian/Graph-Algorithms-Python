import unittest
from domain import Graph
from exceptions import VertexError, EdgeError


class Tests(unittest.TestCase):
    """
    A class that tests the Graph class
    """

    def test_vertices(self) -> None:
        graph = Graph()
        self.assertEqual(graph.vertex_count(), 0)

        graph.add_vertex(2)
        graph.add_vertex(4)
        self.assertEqual(graph.vertex_count(), 2)

        graph.remove_vertex(4)
        self.assertEqual(graph.vertex_count(), 1)

        with self.assertRaises(VertexError):
            graph.add_vertex(2)

        with self.assertRaises(VertexError):
            graph.remove_vertex(100)

    def test_edges(self) -> None:
        graph = Graph(10)
        graph.add_edge(1, 2, 1)
        graph.add_edge(1, 3, 2)
        graph.add_edge(4, 2, 10)
        graph.add_edge(2, 4, 9)
        self.assertEqual(graph.edge_count(), 4)

        graph.remove_edge(1, 2)
        self.assertEqual(graph.edge_count(), 3)

        with self.assertRaises(EdgeError):
            graph.add_edge(1, 3)

        with self.assertRaises(EdgeError):
            graph.add_edge(11, 12)

        self.assertEqual(set(graph.edges_iterator()), {(1, 3, 2), (4, 2, 10), (2, 4, 9)})

    def test_parse_set_of_vertices(self) -> None:
        graph = Graph()
        graph.add_vertex(4)
        graph.add_vertex(1)
        graph.add_vertex(9)

        v = set(graph.vertices_iterator())
        self.assertEqual(v, {1, 4, 9})

        graph.add_vertex(10)
        v = set(graph.vertices_iterator())
        self.assertEqual(v, {1, 4, 9, 10})

    def test_is_edge(self) -> None:
        graph = Graph(4)
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)

        self.assertTrue(graph.is_edge(1, 2))
        self.assertFalse(graph.is_edge(2, 1))

    def test_in_out_degrees(self) -> None:
        graph = Graph(6)
        graph.add_edge(1, 2)
        graph.add_edge(1, 3)
        graph.add_edge(1, 5)
        graph.add_edge(2, 1)
        graph.add_edge(4, 1)

        self.assertEqual(graph.in_degree(1), 2)
        self.assertEqual(graph.out_degree(1), 3)
        self.assertEqual(graph.in_degree(4), 0)
        self.assertEqual(graph.out_degree(4), 1)

    def test_parse_outbound_edge(self) -> None:
        graph = Graph(5)
        graph.add_edge(1, 2)
        graph.add_edge(1, 3)
        graph.add_edge(1, 4)
        graph.add_edge(0, 1)

        self.assertEqual(set(graph.neighbours_iterator(1)), {2, 3, 4})

    def test_parse_inbound_edge(self) -> None:
        graph = Graph(5)
        graph.add_edge(1, 2)
        graph.add_edge(1, 3)
        graph.add_edge(1, 4)
        graph.add_edge(0, 1)

        self.assertEqual(set(graph.transpose_iterator(1)), {0})

    def test_edge_cost(self) -> None:
        graph = Graph(4)
        graph.add_edge(1, 2, 5)
        graph.add_edge(1, 0, 3)
        self.assertEqual(graph.get_edge_cost(1, 2), 5)

        graph.set_edge_cost(1, 2, 10)
        self.assertEqual(graph.get_edge_cost(1, 2), 10)

    def test_copy(self) -> None:
        graph = Graph(4, 7)
        graph_copy = graph.copy()

        graph_copy.remove_vertex(1)
        self.assertEqual(set(graph.vertices_iterator()), {0, 1, 2, 3})
