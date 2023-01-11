from domain import Graph
# 3. Write a program that, given a graph with costs and two vertices,
#    finds the lowest cost walk between the given vertices, or prints a message
#    if there are negative cost cycles accessible from the starting vertex.
# The program will use the Ford's algorithm.


def ford_algorithm(graph: Graph, starting_vertex: int, ending_vertex: int) -> tuple:
    """
    Finds the cheapest path between two vertices using the Bellman–Ford algorithm

    The Bellman-Ford algorithm is slower than Dijkstra's algorithm, but it is more
    versatile because it can detect and report negative cost cycles

    Complexity: O(V x E)
    Where V is the number of vertices and E is the number of edges
    :param graph: a directed graph
    :param starting_vertex: the starting vertex
    :param ending_vertex: the ending vertex
    :return: The cost and the path or None if there are negative cost cycles
    """
    # Step 1: Initialize distances from starting_vertex to all other vertices as INFINITE
    path = [-1] * graph.vertex_count()
    dist = [float("Inf")] * graph.vertex_count()
    dist[starting_vertex] = 0

    # Step 2: Relax all edges V-1 times. A simple shortest path
    # from src to any other vertex can have at-most V-1 edges
    for _ in range(graph.vertex_count() - 1):
        # Update dist value and parent index of the adjacent vertices of the
        # picked vertex. Consider only those vertices which are still in queue
        for s, d, c in graph.edges_iterator():
            if dist[s] != float("Inf") and dist[s] + c < dist[d]:
                dist[d] = dist[s] + c
                path[d] = s

    # Step 3: check for negative-weight cycles. The above step guarantees
    # the shortest distances if graph doesn't contain negative weight
    # cycle. If we get a shorter path, then there is a cycle.
    for s, d, c in graph.edges_iterator():
        if dist[s] != float("Inf") and dist[s] + c < dist[d]:
            return None, None

    return dist[ending_vertex], reconstruct_path_ford(path, ending_vertex)


def reconstruct_path_ford(old_path: list, current_vertex: int) -> list:
    """
    Reconstructs the cheapest path between two vertices in a directed graph
    :param old_path: the list containing the path that needs to be reconstructed
    :param current_vertex: the current vertex
    :return: The reconstructed path or None if it does not exist
    """
    if current_vertex < 0:
        return []

    return reconstruct_path_ford(old_path, old_path[current_vertex]) + [current_vertex]
