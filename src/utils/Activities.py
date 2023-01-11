from domain import Graph
# 4. Write a program that, given a list of activities with duration and
#    list of prerequisites for each activity, does the following:
# - verify if the corresponding graph is a DAG and performs a topological sorting
#   of the activities using the algorithm based on depth-first traversal (Tarjan's algorithm);
# - prints the earliest and the latest starting time for each activity and the total time of the project.
# - prints the critical activities.


def topological_sort_dfs(graph: Graph, vertex: int, sorted_list: list, finished: set, queue: set) -> bool:
    """
    Performs a topological sort of the graph using depth-first traversal
    :param graph: the graph
    :param vertex: the current vertex
    :param sorted_list: the list containing the topological order
    :param finished: the set of handled vertices
    :param queue: the queue
    :return: True if the graph is a DAG, False otherwise
    """
    # we want handle the vertex
    queue.add(vertex)

    # handle every inbound neighbour of the vertex
    for inbound in graph.transpose_iterator(vertex):
        # check if we have a cycle
        if inbound in queue:
            return False
        else:
            # if the vertex was not handled yet
            if inbound not in finished:
                ok = topological_sort_dfs(graph, inbound, sorted_list, finished, queue)
                # cycle reached
                if not ok:
                    return False

    # remove the vertex from the queue
    queue.remove(vertex)

    # add it to the final list
    sorted_list.append(vertex)

    # mark it as handled
    finished.add(vertex)  # it is fully processed
    return True


def dag(graph: Graph) -> list:
    """
    Checks if the graph is a DAG and performs a topological sort of the graph
    :param graph: the graph
    :return: the graph sorted topologically
    """
    # the final list containing the topological order
    sorted_list = []
    # store handled vertices
    finished = set()
    # store the queue
    queue = set()
    for vertex in graph.vertices_iterator():
        # loop through every vertex that was not handled yet
        if vertex not in finished:
            ok = topological_sort_dfs(graph, vertex, sorted_list, finished, queue)

            # cycle detected, not a DAG
            if not ok:
                return []

    return sorted_list


def compute_times(graph: Graph, sorted_list: list) -> tuple:
    """
    Computes the earliest and latest starting time for each activity and lists critical activities
    :param graph: the graph
    :param sorted_list: the topological order of the graph
    :return: the earliest and latest starting time for each activity and the critical activities
    """
    first = -1
    last = len(sorted_list)

    # add the placeholder nodes: first and last
    graph.add_vertex(first)
    graph.add_vertex(last)

    # insert the first placeholder activity
    sorted_list.insert(0, first)
    graph.durations[first] = 0

    # add the edges between the first and the vertices with no inbound
    for vertex in graph.vertices_iterator():
        if graph.in_degree(vertex) == 0 and vertex != first and vertex != last:
            graph.add_edge(first, vertex)

    # insert the placeholder last activity
    sorted_list.append(last)
    graph.durations[last] = 0

    # add the edges between the vertices with no outbound and the last
    for vertex in graph.vertices_iterator():
        if graph.out_degree(vertex) == 0 and vertex != first and vertex != last:
            graph.add_edge(vertex, last)

    # initialise the dictionaries for earliest_start_time and earliest_end_time
    earliest_start_time = dict()
    earliest_end_time = dict()
    for vertex in graph.vertices_iterator():
        earliest_start_time[vertex] = 0
        earliest_end_time[vertex] = 0

    # initialise the dictionaries for latest_start_time and latest_end_time
    latest_start_time = dict()
    latest_end_time = dict()
    for vertex in graph.vertices_iterator():
        latest_start_time[vertex] = float("Inf")
        latest_end_time[vertex] = float("Inf")

    # compute the earliest start and end time for each activity
    for i in range(1, len(sorted_list)):
        # take as earliest start time the maximum earliest end time of the predecessors
        for inbound in graph.transpose_iterator(sorted_list[i]):
            earliest_start_time[sorted_list[i]] = \
                max(earliest_start_time[sorted_list[i]], earliest_end_time[inbound])
        # the earliest end time will be the earliest start time + duration of activity
        earliest_end_time[sorted_list[i]] = \
            earliest_start_time[sorted_list[i]] + graph.durations[sorted_list[i]]

    # compute the latest start and end time for each activity
    latest_end_time[last] = earliest_end_time[last]
    latest_start_time[last] = latest_end_time[last] - graph.durations[last]
    latest_start_time[first] = 0
    latest_end_time[first] = 0

    # compute the latest start and end time of each activity
    for i in range(len(sorted_list) - 1, 0, -1):
        # take as latest end time the minimum of the latest start time of the outbounds
        for outbound in graph.neighbours_iterator(sorted_list[i]):
            latest_end_time[sorted_list[i]] = min(latest_end_time[sorted_list[i]], latest_start_time[outbound])
        # the latest start time will be the latest end time - duration of activity
        latest_start_time[sorted_list[i]] = \
            latest_end_time[sorted_list[i]] - graph.durations[sorted_list[i]]

    # remove the placeholder nodes
    sorted_list.pop(0)
    sorted_list.pop()
    graph.remove_vertex(first)
    graph.remove_vertex(last)

    # determine the critical activities
    critical_activities = []
    for activity in sorted_list:
        if earliest_start_time[activity] == latest_start_time[activity]:
            critical_activities.append(activity)

    return earliest_start_time, earliest_end_time, latest_start_time, latest_end_time, critical_activities
