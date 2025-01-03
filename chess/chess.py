class Piece():
    def __init__(self, code):
        self.code = code
        self.kind = code[0]
        self.player = code[1]



class Board():
    def __init__(self):
        self.pieces = {}
        

    def set_piece(self, piece, position):
        self.pieces[position] = piece
    
    def get_piece(self, position):
        return self.pieces.get(position, None)


    def display_board_state(self):
        string = ""
        row_count = 8
        letters = "abcdefgh"
        while row_count > 0:
            row = f"{row_count}:"
            for letter in letters:
                split = "|"
                if letter == "a":
                    split = ""
                position = letter + str(row_count)
                piece = self.get_piece(position)
                if isinstance(piece, Piece):
                    row += f"{split} {piece.code} "
                else:
                    row += f"{split}    "
            string += row
            string += ('\n')
            row_count -= 1
        string += "   a    b    c    d    e    f    g    h"
        return string
    

    def move_piece(self, old_pos, new_pos):
        piece = self.pieces[old_pos]
        if not isinstance(piece, Piece):
            raise ValueError("Illegal move: no piece at start position")
        if isinstance(self.pieces.get(new_pos, None), Piece) and self.pieces[new_pos].player == piece.player:
            raise ValueError("Illegal move: cannot move to friendly territory")
        self.pieces.pop(old_pos)
        self.pieces[new_pos] = piece

    def process_movements(self, movements):
        for movement in movements:
            self.move_piece(movement[0], movement[1])
    
    def read_movement_file(self, file_name):
        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()
        moves = []
        for line in lines:
            splitted = line.strip("\n").split(" - ")
            moves.append((splitted[0], splitted[1]))
        return moves


    def board_save_state(self, file_name):
        lines = ""
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(self.display_board_state())

    

    






board = Board()
#alle pieces zetten
# Plaats de witte stukken 
board.set_piece(Piece("Rw"), "a1") 
board.set_piece(Piece("Nw"), "b1") 
board.set_piece(Piece("Bw"), "c1") 
board.set_piece(Piece("Qw"), "d1") 
board.set_piece(Piece("Kw"), "e1") 
board.set_piece(Piece("Bw"), "f1") 
board.set_piece(Piece("Nw"), "g1") 
board.set_piece(Piece("Rw"), "h1") 
for col in 'abcdefgh': 
    board.set_piece(Piece("Pw"), f"{col}2") 

# Plaats de zwarte stukken 
board.set_piece(Piece("Rb"), "a8") 
board.set_piece(Piece("Nb"), "b8") 
board.set_piece(Piece("Bb"), "c8") 
board.set_piece(Piece("Qb"), "d8") 
board.set_piece(Piece("Kb"), "e8") 
board.set_piece(Piece("Bb"), "f8") 
board.set_piece(Piece("Nb"), "g8") 
board.set_piece(Piece("Rb"), "h8") 
for col in 'abcdefgh': 
    board.set_piece(Piece("Pb"),f"{col}7")


board.process_movements([("d1","d5"),("d5","e5")])
board.process_movements(board.read_movement_file("sample_movements.txt"))
print(board.display_board_state())
board.board_save_state("output_board.txt")





    
