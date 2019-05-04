from piece import Piece

class Player():
    def __init__(self, name,curr_position, piece_name):
        self.name = name
        self.piece = Piece(piece_name)
        self.current_position = tuple((curr_position[0],curr_position[1]))

    def get_moves(self):
        move_list = self.piece.step.move_list
        moves = []
        for move in move_list:
            x = move[0]+self.current_position[0]
            y = move[1]+self.current_position[1]
            moves.append((x,y))

        return moves