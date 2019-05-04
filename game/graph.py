class Vertex():
    def __init__(self, node):
        self.id = node #it will be a tuple of coordinates (x,y)
        self.adjacent = {}

    def get_id(self):
        return self.id

    def add_neighbour(self, neighbour, cost):
        if neighbour not in self.adjacent:
            self.adjacent[neighbour] = cost

    def get_connections(self):
        return self.adjacent

    def get_cost(self, neighbour):
        return self.adjacent[neighbour]

class Graph():
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def add_vertex(self, node):
        if node not in self.vertices:
            new_vertex = Vertex(node)
            self.vertices[node] = new_vertex
            self.num_vertices +=1
            return new_vertex

    def add_edge(self,vertex1,vertex2, cost):

        if vertex1 not in self.vertices:
            self.add_vertex(vertex1)
        if vertex2 not in self.vertices:
            self.add_vertex(vertex1)

        self.vertices[vertex1].add_neighbour(self.vertices[vertex2],cost)

        self.vertices[vertex2].add_neighbour(self.vertices[vertex1],cost)

    def get_vertices(self):
        return self.vertices.keys()

    def BFS(self, start_vertex, step):
        visited = {}
        for v in self.vertices:
            visited[v] = False

        queue = []
        queue.append(start_vertex)

        visited[start_vertex] = True
        i=0
        while queue:
            ele = queue.pop(0)

            i+=1
            for move in step.move_list:
                x = ele[0]+move[0]
                y = ele[1]+move[1]
                node = (x,y)
                if node in self.vertices:
                    if visited[node]==False:
                        self.add_edge(ele,node,i)
                        queue.append(node)
                        visited[node]=True


    def find_shortest_path_cost(self,v):
        connection_list = self.vertices[v].get_connections()
        minimum_cost = float('inf')
        for neighbour in connection_list:
            cost = self.vertices[v].get_cost(neighbour)
            if cost< minimum_cost:
                minimum_cost = cost
        return minimum_cost