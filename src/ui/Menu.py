from domain import Graph
from utils import (
    read_file, write_file, read_from_activities_file,
    backwards_breadth_first_search, ford_algorithm,
    dag, compute_times
)


class Menu:
    """
    A class that handles the menu of the program.
    """

    def __init__(self) -> None:
        """
        Creates an instance of the Menu class.
        """
        self.__graph = Graph()

        self.__menu_options = ["Exit", "Read from file", "Write to file",
                               "Print vertex count", "Print edge count",
                               "Print list of vertices", "Print list of edges",
                               "Generate empty graph", "Generate graph with n vertices",
                               "Generate graph with n vertices and m random edges", "Add vertex",
                               "Add edge", "Remove vertex", "Remove edge", "Change edge cost",
                               "Print edge cost", "Print in degree of vertex",
                               "Print out degree of vertex", "Check if a vertex belongs to the graph",
                               "Check if an edge belongs to the graph",
                               "Print list of outbound neighbours of a vertex",
                               "Print list of inbound neighbours of a vertex",
                               "Find the lowest length path between two vertices using BFS backwards",
                               "Find the lowest cost walk between two vertices using Ford's algorithm",
                               "Read from an activities file", "Perform a topological sort", "Show activities"]

    def empty_graph(self) -> None:
        """
        Generates an empty graph.
        """
        try:
            self.__graph = Graph()
            print("INFO: Generated an empty graph.")
        except Exception as e:
            print(e)

    def graph_with_vertices(self) -> None:
        """
        Generates a graph with n vertices.
        """
        vertex_count = Menu.get_input("Vertex count: ")

        try:
            self.__graph = Graph(vertex_count)
            print(f"INFO: Generated graph with {vertex_count} vertices.")
        except Exception as e:
            print(e)

    def graph_with_vertices_and_edges(self) -> None:
        """
        Generates a graph with n vertices and m random edges.
        """
        vertex_count = Menu.get_input("Vertex count: ")
        edge_count = Menu.get_input("Edge count: ")
        max_edge_count = vertex_count * (vertex_count - 1)

        if edge_count > max_edge_count:
            print(f"ERROR: The maximum edge count is {max_edge_count}.")
            return

        try:
            self.__graph = Graph(vertex_count, edge_count)
            print(f"INFO: Generated graph with {vertex_count} vertices and {edge_count} random edges.")
        except Exception as e:
            print(e)

    def add_vertex(self) -> None:
        """
        Adds a vertex to the graph.
        """
        vertex = Menu.get_input("Vertex to add: ")

        try:
            self.__graph.add_vertex(vertex)
            print(f"INFO: Added vertex {vertex} to the graph.")
        except Exception as e:
            print(e)

    def add_edge(self) -> None:
        """
        Adds an edge to the graph.
        """
        vertex1 = Menu.get_input("First vertex: ")
        vertex2 = Menu.get_input("Second vertex: ")
        cost = Menu.get_input("Edge cost: ")

        try:
            self.__graph.add_edge(vertex1, vertex2, cost)
            print(f"INFO: Added edge ({vertex1}, {vertex2}) with cost {cost} to the graph.")
        except Exception as e:
            print(e)

    def remove_vertex(self) -> None:
        """
        Removes a vertex from the graph.
        """
        vertex = Menu.get_input("Vertex to remove: ")

        try:
            self.__graph.remove_vertex(vertex)
            print(f"INFO: Removed vertex {vertex} from the graph.")
        except Exception as e:
            print(e)

    def remove_edge(self) -> None:
        """
        Removes an edge from the graph.
        """
        vertex1 = Menu.get_input("First vertex: ")
        vertex2 = Menu.get_input("Second vertex: ")

        try:
            self.__graph.remove_edge(vertex1, vertex2)
            print(f"INFO: Removed edge ({vertex1}, {vertex2}) from the graph.")
        except Exception as e:
            print(e)

    def change_edge_cost(self) -> None:
        """
        Changes the cost of an edge.
        """
        vertex1 = Menu.get_input("First vertex: ")
        vertex2 = Menu.get_input("Second vertex: ")
        cost = Menu.get_input("New cost: ")

        try:
            self.__graph.set_edge_cost(vertex1, vertex2, cost)
            print(f"INFO: Changed the cost of the edge ({vertex1}, {vertex2}) to {cost}.")
        except Exception as e:
            print(e)

    def print_edge_cost(self) -> None:
        """
        Prints the cost of an edge.
        """
        vertex1 = Menu.get_input("First vertex: ")
        vertex2 = Menu.get_input("Second vertex: ")

        try:
            print(f"INFO: The cost of edge ({vertex1}, {vertex2}) is {self.__graph.get_edge_cost(vertex1, vertex2)}.")
        except Exception as e:
            print(e)

    def print_in_degree(self) -> None:
        """
        Prints the in degree of a vertex.
        """
        vertex = Menu.get_input("Vertex: ")

        try:
            print(f"INFO: The in degree of vertex {vertex} is {self.__graph.in_degree(vertex)}.")
        except Exception as e:
            print(e)

    def print_out_degree(self) -> None:
        """
        Prints the out degree of a vertex.
        """
        vertex = Menu.get_input("Vertex: ")

        try:
            print(f"INFO: The out degree of vertex {vertex} is {self.__graph.out_degree(vertex)}.")
        except Exception as e:
            print(e)

    def print_vertex_count(self) -> None:
        """
        Prints the number of vertices in the graph.
        """
        print(f"INFO: The graph has {self.__graph.vertex_count()} vertices.")

    def print_edge_count(self) -> None:
        """
        Prints the number of edges in the graph.
        """
        print(f"INFO: The graph has {self.__graph.edge_count()} edges.")

    def is_vertex(self) -> None:
        """
        Checks if a vertex belongs to the graph.
        """
        vertex = Menu.get_input("Vertex: ")

        try:
            if self.__graph.is_vertex(vertex):
                print(f"INFO: Vertex {vertex} belongs to the graph.")
            else:
                print(f"INFO: Vertex {vertex} does not belong to the graph.")
        except Exception as e:
            print(e)

    def is_edge(self) -> None:
        """
        Checks if an edge belongs to the graph.
        """
        vertex1 = Menu.get_input("First vertex: ")
        vertex2 = Menu.get_input("Second vertex: ")

        try:
            if self.__graph.is_edge(vertex1, vertex2):
                print(f"INFO: Edge ({vertex1}, {vertex2}) belongs to the graph.")
            else:
                print(f"INFO: Edge ({vertex1}, {vertex2}) does not belong to the graph.")
        except Exception as e:
            print(e)

    def print_vertex_list(self) -> None:
        """
        Prints the list of vertices in the graph.
        """
        if self.__graph.vertex_count() == 0:
            print("INFO: The graph has no vertices.")
            return None

        print("Vertices: ", end="")
        for node in self.__graph.vertices_iterator():
            print(node, end=" ")

        print()

    def print_neighbour_list(self) -> None:
        """
        Prints the list of outbound neighbours of a vertex.
        """
        if self.__graph.vertex_count() == 0:
            print("INFO: The graph has no vertices.")
            return None

        vertex = Menu.get_input("Vertex: ")
        result = "Outbound: "

        try:
            has_neighbour = False
            for node in self.__graph.neighbours_iterator(vertex):
                result += f"{node} "
                has_neighbour = True

            if not has_neighbour:
                print("INFO: The vertex has no neighbours.")
            else:
                print(result)
        except Exception as e:
            print(e)

    def print_transpose_list(self) -> None:
        """
        Prints the list of inbound neighbours of a vertex.
        """
        if self.__graph.vertex_count() == 0:
            print("INFO: The graph has no vertices.")
            return None

        vertex = Menu.get_input("Vertex: ")
        result = "Inbound: "

        try:
            has_neighbour = False
            for node in self.__graph.transpose_iterator(vertex):
                result += f"{node} "
                has_neighbour = True

            if not has_neighbour:
                print("INFO: The vertex has no neighbours.")
            else:
                print(result)
        except Exception as e:
            print(e)

    def print_edges(self) -> None:
        """
        Prints the list of edges in the graph.
        """
        has_edges = False

        for triplet in self.__graph.edges_iterator():
            print(f"Edge ({triplet[0]}, {triplet[1]}) with cost {triplet[2]}.")
            has_edges = True
        if not has_edges:
            print("INFO: The graph has no edges.")

    def print_menu(self) -> None:
        """
        Prints the menu.
        """
        for i in range(100):
            print()

        for i in range(len(self.__menu_options)):
            print((" " if i < 10 else "") + str(i) + ". " + self.__menu_options[i])
        print()

    def run(self) -> None:
        """
        Clears the console window and displays the user interface,
        then asks for input and calls the handler function
        """
        while True:
            self.print_menu()
            option = Menu.get_input("Option: ")

            if option == 0:
                print("INFO: Quitting.\n")
                input("Press <ENTER> to continue.")

                return None

            self.handle_menu_option(option)

    def handle_menu_option(self, option: int) -> None:
        """
        Handles the given menu option using the list of complex numbers
        :param option: The menu option that was selected by the user
        """
        if option == 1:
            self.read_file()
        elif option == 2:
            self.write_file()
        elif option == 3:
            self.print_vertex_count()
        elif option == 4:
            self.print_edge_count()
        elif option == 5:
            self.print_vertex_list()
        elif option == 6:
            self.print_edges()
        elif option == 7:
            self.empty_graph()
        elif option == 8:
            self.graph_with_vertices()
        elif option == 9:
            self.graph_with_vertices_and_edges()
        elif option == 10:
            self.add_vertex()
        elif option == 11:
            self.add_edge()
        elif option == 12:
            self.remove_vertex()
        elif option == 13:
            self.remove_edge()
        elif option == 14:
            self.change_edge_cost()
        elif option == 15:
            self.print_edge_cost()
        elif option == 16:
            self.print_in_degree()
        elif option == 17:
            self.print_out_degree()
        elif option == 18:
            self.is_vertex()
        elif option == 19:
            self.is_edge()
        elif option == 20:
            self.print_neighbour_list()
        elif option == 21:
            self.print_transpose_list()
        elif option == 22:
            self.path_between_vertices_bfs()
        elif option == 23:
            self.lowest_cost_path_ford()
        elif option == 24:
            self.get_graph_from_activities_file()
        elif option == 25:
            self.print_topological_sort_result()
        elif option == 26:
            self.show_activities()
        else:
            print("ERROR: Invalid menu option!")

        print()
        input("Press <ENTER> to continue.")

    def read_file(self) -> None:
        """
        Reads a graph from a file.
        """
        path = input("File name: ")

        try:
            self.__graph = read_file(path)
            print("INFO: Graph read from file successfully.")
        except Exception as e:
            print(e)

    def write_file(self) -> None:
        """
        Writes the graph to a file.
        """
        path = input("File name: ")

        try:
            write_file(path, self.__graph)
            print("INFO: Graph written to file successfully.")
        except Exception as e:
            print(e)

    def get_graph_from_activities_file(self) -> None:
        """
        Reads a graph from a file containing activities.
        """
        path = input("File name: ")

        try:
            self.__graph = read_from_activities_file(path)
            print("INFO: Graph read from file successfully.")
        except Exception as e:
            print(e)

    def path_between_vertices_bfs(self) -> None:
        """
        Checks if there is a path between two vertices using BFS backwards.
        """
        vertex1 = Menu.get_input("Source vertex: ")
        vertex2 = Menu.get_input("Destination vertex: ")
        if not self.__graph.is_vertex(vertex1) or not self.__graph.is_vertex(vertex2):
            print("ERROR: One or more vertices do not belong to the graph.")
            return None

        path = backwards_breadth_first_search(self.__graph, vertex1, vertex2)
        if path is None or len(path) == 0:
            print("INFO: There is no path between the given vertices.")
            return None

        if len(path) == 1:
            print(f"INFO: The path of length 1 is: {path[0]} > {path[0]}")
            return None

        result = f"INFO: The path of length {len(path) - 1} is: "
        for vertex in path:
            result += str(vertex) + " > "

        print(result[:-3])

    def lowest_cost_path_ford(self) -> None:
        """
        Finds the lowest cost path between two vertices using the Bellman-Ford algorithm.
        """
        vertex1 = Menu.get_input("Source vertex: ")
        vertex2 = Menu.get_input("Destination vertex: ")
        if not self.__graph.is_vertex(vertex1) or not self.__graph.is_vertex(vertex2):
            print("ERROR: One or more vertices do not belong to the graph.")
            return None

        cost, path = ford_algorithm(self.__graph, vertex1, vertex2)

        if path is None:
            print("INFO: The graph contains negative cost cycles.")
        else:
            if len(path) == 1:
                print(f"INFO: The cheapest path costs {cost} and is: {path[0]} > {path[0]}")
                return None

            result = f"INFO: The cheapest path costs {cost} and is: "
            for vertex in path:
                result += str(vertex) + " > "

            print(result[:-3])

    def print_topological_sort_result(self) -> None:
        """
        Prints the result of the topological sort algorithm.
        """
        sorted_graph = dag(self.__graph)
        if len(sorted_graph) == 0:
            print("INFO: The graph is not a DAG.")
            return

        print("Topological sort: ", end="")
        for vertex in sorted_graph:
            print(vertex, end=" ")

        print()

    def show_activities(self) -> None:
        """
        Shows the times of the activities in the graph.
        """
        sorted_graph = dag(self.__graph)
        if len(sorted_graph) == 0:
            print("INFO: The graph is not a DAG.")
            return

        print(f"Topological sorting: {sorted_graph}")
        earliest_start_time, earliest_end_time, latest_start_time, latest_end_time, critical_activities =\
            compute_times(self.__graph, sorted_graph)

        for vertex in sorted_graph:
            print(f"{vertex}: Start: {earliest_start_time[vertex]} - "
                  f"{earliest_end_time[vertex]} | "
                  f"End: {latest_start_time[vertex]} - "
                  f"{latest_end_time[vertex]}")

        print(f"Total time: {earliest_start_time[len(sorted_graph)]}")
        print("\nCritical activities: ", end="")

        for activity in critical_activities:
            print(activity, end=" ")

        print()

    @staticmethod
    def get_input(prompt: str) -> int:
        """
        Gets input from the user and returns it as an integer
        :param prompt: the prompt that is shown to the user for input
        :return: a valid integer
        """
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                print()
                print("ERROR: Invalid input!")
