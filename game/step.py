from constants import ChessPieceMoves

class Step():
    def __init__(self):
        self.move_list = []
        return

    def set(self, piece_name):
        if ChessPieceMoves[piece_name.upper()].value == "2.5":
            self.move_list = [(-2,-1),(-2,1),(2,1),(2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
        return self
        #we can configure any number of steps

    def get(self):
        return self