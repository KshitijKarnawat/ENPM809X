import heapq

# Define a Vertex class to store contact information
class Vertex:
    def __init__(self, id, start_time, end_time, sender, receiver, owlt):
        self.id = id
        self.start_time = start_time
        self.end_time = end_time
        self.sender = sender
        self.receiver = receiver
        self.owlt = owlt
        self.adjacent = {}

    def add_neighbor(self, neighbor, weight):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]


# Define a Graph class to store the contact graph
class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex.id] = vertex

    def get_vertex(self, id):
        if id in self.vertices:
            return self.vertices[id]
        else:
            return None

    def get_vertices(self):
        return self.vertices.keys()


# Define the Dijkstra algorithm function
def dijkstra(graph, start, end):
    # Initialize the priority queue
    queue = [(0, start)]
    # Initialize the distances dictionary
    distances = {start: 0}
    # Initialize the previous dictionary
    previous = {}

    while queue:
        # Get the vertex with the smallest distance from the start node
        (cost, current_vertex) = heapq.heappop(queue)

        # If we have reached the end node, return the path
        if current_vertex == end:
            path = []
            while current_vertex in previous:
                path.append(current_vertex)
                current_vertex = previous[current_vertex]
            path.append(start)
            path.reverse()
            return path, distances[end]

        # Otherwise, update the distances to the adjacent vertices
        for next_vertex in graph.get_vertex(current_vertex).get_connections():
            new_cost = distances[current_vertex] + graph.get_vertex(current_vertex).get_weight(next_vertex)
            if next_vertex not in distances or new_cost < distances[next_vertex]:
                distances[next_vertex] = new_cost
                previous[next_vertex] = current_vertex
                heapq.heappush(queue, (new_cost, next_vertex))

    # If we have explored all possible paths and not reached the end node, return None
    return None, None


# Read the contact graph info from the file and create a graph object
filename = "ContactList.txt"
graph = Graph()

with open(filename) as f:
    for line in f:
        id, start_time, end_time, sender, receiver, owlt = line.split()
        vertex1 = graph.get_vertex(sender)
        if vertex1 is None:
            vertex1 = Vertex(sender, 0, float('inf'), sender, None, None)
            graph.add_vertex(vertex1)
        vertex2 = graph.get_vertex(receiver)
        if vertex2 is None:
            vertex2 = Vertex(receiver, 0, float('inf'), receiver, None, None)
            graph.add_vertex(vertex2)
        vertex1.add_neighbor(receiver, float(end_time) - float(start_time))
        vertex2.add_neighbor(sender, float(end_time) - float(start_time))

# Use Dijkstra to find the optimal path from node #1 to node #12
start_node = "1"
end_node = "12"
path, best_arrival_time = dijkstra(graph, start_node, end_node)
print(path)
print(best_arrival_time)
# Print the contact ids corresponding to the optimal path and the resulting best arrival time
# if path:
#     print("
