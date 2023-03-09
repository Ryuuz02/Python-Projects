from colorama import Fore


class ChessBoard:
    def __init__(self, rows=8, cols=8):
        self.board = []
        self.rows = rows
        self.cols = cols
        for row in range(0, rows):
            self.board.append([])
        for col in range(0, cols):
            for row in range(0, rows):
                self.board[col].append("")
        for row in range(1, rows + 1):
            if row == 1 or row == 8:
                unit = ""
                for col in range(1, 9):
                    if col == 1 or col == 8:
                        unit = "R"
                    elif col == 2 or col == 7:
                        unit = "N"
                    elif col == 3 or col == 6:
                        unit = "B"
                    elif row == 1:
                        if col == 4:
                            unit = "Q"
                        elif col == 5:
                            unit = "K"
                    else:
                        if col == 5:
                            unit = "Q"
                        elif col == 4:
                            unit = "K"
                    self.replace_spot(unit, col, row)
            elif row == 2:
                for col in range(1, 9):
                    self.replace_spot("P", col, row)
            elif row == 7:
                for col in range(1, 9):
                    self.replace_spot("P", col, row)
            else:
                for col in range(1, 9):
                    self.replace_spot("_", col, row)

    def print_board(self):
        a_to_h = ["A", "B", "C", "D", "E", "F", "G", "H"]
        print("   " + " ".join(a_to_h))
        for row in range(0, self.rows):
            current_line = self.board[row]
            print_line = [piece.print() for piece in current_line]
            if row in [0, 1]:
                print(Fore.RESET + str(8 - row) + Fore.GREEN + " |" + "|".join(print_line) + "|")
            elif row in [6, 7]:
                print(Fore.RESET + str(8 - row) + Fore.BLUE + " |" + "|".join(print_line) + "|")
            else:
                print(Fore.RESET + str(8 - row) + " |" + "|".join(print_line) + "|")

    def replace_spot(self, new_piece, x, y):
        index_accounted_y = y - self.cols
        index_accounted_x = x - self.rows
        piece = dict_of_pieces[new_piece](Fore.BLUE, x, y)
        self.board[-index_accounted_y][index_accounted_x] = piece


class ChessPiece:
    def __init__(self, symbol, color, x, y):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.color = color

    def move(self):
        pass

    def print(self):
        return self.symbol


class Empty(ChessPiece):
    def __init__(self, color, x, y):
        super().__init__("_", Fore.RESET, x, y)


class Pawn(ChessPiece):
    def __init__(self, color, x, y):
        super().__init__("P", color, x, y)

    def move(self):
        pass


class Rook(ChessPiece):
    def __init__(self, color, x, y):
        super().__init__("R", color, x, y)

    def move(self):
        pass


class Knight(ChessPiece):
    def __init__(self, color, x, y):
        super().__init__("N", color, x, y)

    def move(self):
        pass


class Queen(ChessPiece):
    def __init__(self, color, x, y):
        super().__init__("Q", color, x, y)

    def move(self):
        pass


class Bishop(ChessPiece):
    def __init__(self, color, x, y):
        super().__init__("B", color, x, y)

    def move(self):
        pass


class King(ChessPiece):
    def __init__(self, color, x, y):
        super().__init__("K", color, x, y)

    def move(self):
        pass


dict_of_pieces = {"P": Pawn,
                  "R": Rook,
                  "Q": Queen,
                  "K": King,
                  "B": Bishop,
                  "N": Knight,
                  "_": Empty
                  }
chess_board = ChessBoard()
chess_board.print_board()
