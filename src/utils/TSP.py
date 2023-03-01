from domain import Graph
# 6. Given a digraph with costs, find a minimum cost Hamiltonian cycle (i.e., solve the TSP)


def get_minimum_cost_hamiltonian(graph: Graph, start: int, visited: list) -> int:
    """
    Computes the minimum cost Hamiltonian cycle (Travelling Salesman Problem)

    :param graph: a weighted directed graph
    :param start: the starting vertex
    :param visited: a list that will keep track of the already visited vertices and the final cycle
    :return: the cost of the minimum cost Hamiltonian cycle
    """
    visited.append(start)
    current_vertex = start
    minimum_cost = 0

    # loop through every unvisited vertex
    while len(visited) != graph.vertex_count():
        current_minimum = float("Inf")
        other_vertex = -1

        # we go through the neighbours of the current vertex
        for outbound in graph.neighbours_iterator(current_vertex):
            current_cost = graph.get_edge_cost(current_vertex, outbound)

            if outbound not in visited and current_cost < current_minimum:
                current_minimum = current_cost
                other_vertex = outbound

        # check the last edge
        if len(visited) == graph.vertex_count() - 1 and graph.is_edge(current_vertex, start):
            current_cost = graph.get_edge_cost(current_vertex, start)

            if current_cost < current_minimum:
                current_minimum = current_cost
                other_vertex = start

        # check if there is another vertex
        if other_vertex != -1:
            minimum_cost += current_minimum
            visited.append(other_vertex)
            current_vertex = other_vertex
        else: # if there is no other vertex, we start from the first unvisited vertex
            for vertex in graph.vertices_iterator():
                if vertex not in visited:
                    current_vertex = vertex
                    break

        # while loop end for visibility

    # check the last edge
    if current_vertex != start:
        visited.append(start)
        minimum_cost += graph.get_edge_cost(current_vertex, start)

    # return the minimum cost
    return minimum_cost
