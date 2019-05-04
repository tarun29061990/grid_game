
from graph import Graph
from player import Player

class Game():
    def __init__(self, game_name, rows, columns, blocked_locations):
        self.name = game_name
        self.rows = rows
        self.columns = columns
        self.graph = self.create_graph()
        self.blocked_locations = blocked_locations
        self.players = []

    def add_destination(self, x,y):

        self.destination = tuple((x,y))
        return self.destination

    def add_edges(self,start_coordinate,step):
        self.graph.BFS(start_coordinate,step)

    def create_graph(self):
        g = Graph()
        for row in range(0,self.rows):
            for col in range(0,self.columns):
                node = tuple((row,col))
                g.add_vertex(node)

        return g

    def add_players(self, player):
        if player not in self.players:
            self.players.append(player)

        return self.players

    def add_blocked_locations(self,x,y):
        if (x,y) not in self.blocked_locations:
            self.blocked_locations.append((x,y))
        return tuple((x,y))

    def play(self):
        i=0
        while 1:
            curr_player = self.players[i]
            destination_vertex_cost = {"cost":float('inf'), "vertex":""}

            moves = curr_player.get_moves()
            previous_move = tuple()
            for move in moves:
                node = tuple((move[0],move[1]))
                if node in self.graph.vertices and node not in self.blocked_locations:
                    cost = self.graph.find_shortest_path_cost(node)
                    if cost and cost<destination_vertex_cost["cost"]:
                        destination_vertex_cost["cost"] = cost
                        destination_vertex_cost["vertex"] = node

            if destination_vertex_cost['cost'] != float('inf') and previous_move != destination_vertex_cost["vertex"]:
                previous_move = destination_vertex_cost["vertex"]
                print(curr_player.name+" moved from "+str(curr_player.current_position)+" to "+str(destination_vertex_cost["vertex"]), end='\n')

                curr_player.current_position = destination_vertex_cost["vertex"]
                if curr_player.current_position == destination_tuple:
                    print(curr_player.name+" is the winner")
                    return

                i = i^1

g = Game('chess',8,8,[(3,4),(6,7)])
destination_tuple = g.add_destination(4,4)

p1 = Player('Tarun', (1,2), 'knight')
p2 = Player('Other', (2,4), 'knight')

g.add_players(p1)
g.add_players(p2)

g.add_edges(destination_tuple, p1.piece.step)

g.play()