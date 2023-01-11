from typing import Union
from domain import Graph
# 2. Write a program that, given a directed graph and two vertices, finds the lowest length
#    path between them, by using a backward breadth-first search from the ending vertex.


def backwards_breadth_first_search(graph: Graph, starting_vertex: int, ending_vertex: int) -> list:
    """
    Breadth first search algorithm done backwards (from the ending vertex)
    :param graph: a directed graph
    :param starting_vertex: the starting vertex
    :param ending_vertex: the ending vertex
    :return: The path or None if it does not exist
    """
    # Store the next vertex of each parsed vertex so that the path can be reconstructed
    path = [-1] * graph.vertex_count()
    # Only visit each vertex once
    visited = [False] * graph.vertex_count()
    # List of vertices whose inbound neighbours we need to parse
    queue = [ending_vertex]

    while queue:
        vertex = queue.pop(0)
        visited[vertex] = True

        for inbound in graph.transpose_iterator(vertex):
            if not visited[inbound]:
                queue.append(inbound)
                visited[inbound] = True
                path[inbound] = vertex

    return reconstruct_path_bfs(path, starting_vertex, ending_vertex)


def reconstruct_path_bfs(old_path: list, starting_vertex: int, ending_vertex: int) -> Union[list, None]:
    """
    Reconstructs the shortest path between two vertices in a directed graph
    :param old_path: the list containing the path that needs to be reconstructed
    :param starting_vertex: the starting vertex
    :param ending_vertex: the ending vertex
    :return: The reconstructed path or None if it does not exist
    """
    path = [starting_vertex]
    destination = starting_vertex
    
    while destination != ending_vertex:
        if destination == -1:
            return None

        starting_vertex = destination
        destination = old_path[starting_vertex]
        path.append(destination)

    return path
