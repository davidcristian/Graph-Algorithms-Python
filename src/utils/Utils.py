import os
from domain import Graph


def read_file(file_path: str) -> Graph:
    file_path = os.path.join(os.path.realpath(__file__), "..", "..", "resources", file_path)
    if os.stat(file_path).st_size == 0:
        raise FileNotFoundError("ERROR: The file is empty or does not exist!")

    with open(file_path, "r") as file:
        vertex_count, edge_count = map(int, file.readline().split())
        graph = Graph(vertex_count)

        for _ in range(edge_count):
            vertex1, vertex2, cost = map(int, file.readline().split())
            graph.add_edge(vertex1, vertex2, cost)

    return graph


def write_file(file_path: str, graph: Graph) -> None:
    if graph.vertex_count() == 0:
        raise ValueError("ERROR: The graph is empty!")

    file_path = os.path.join(os.path.realpath(__file__), "..", "..", "resources", file_path)

    with open(file_path, "w") as file:
        file.truncate(0)
        file.write(f"{graph.vertex_count()} {graph.edge_count()}\n")

        for vertex in graph.vertices_iterator():
            for neighbour in graph.neighbours_iterator(vertex):
                file.write(f"{vertex} {neighbour} {graph.get_edge_cost(vertex, neighbour)}\n")


def read_from_activities_file(file_path: str) -> Graph:
    file_path = os.path.join(os.path.realpath(__file__), "..", "..", "resources", file_path)
    if os.stat(file_path).st_size == 0:
        raise FileNotFoundError("ERROR: The file is empty or does not exist!")

    with open(file_path, "r") as file:
        lines = file.readlines()
        graph = Graph(0, 0)

        # Add the edges
        for index in range(0, len(lines)):
            tokens = lines[index].split()
            if len(tokens) == 0:
                break

            node = int(tokens[0])
            time = int(tokens[1])
            if not graph.is_vertex(node):
                graph.add_vertex(node)

            graph.durations[node] = time
            if tokens[2] == "-":
                continue

            neighbours_tokens = tokens[2].split(",")
            neighbours = [int(neighbour) for neighbour in neighbours_tokens]

            for neighbour in neighbours:
                if neighbour != "-":
                    if not graph.is_vertex(neighbour):
                        graph.add_vertex(neighbour)

                    graph.add_edge(neighbour, node)

        return graph
