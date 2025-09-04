from chess_pieces import Piece
from typing import List

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]

    def set_position(self, position: tuple, piece: Piece = None, update_position: bool = True):
        row, col = position
        if not piece:
            piece = 0
        else:
            x, y = piece.position
            if update_position:
                piece.position = (row, col)
            self.grid[x][y] = 0

        self.grid[row][col] = piece

    def is_enemy(self, position: tuple, color: str) -> bool:
        row, col = position
        target_piece = self.grid[row][col]
        if color == "white" and self.grid[row][col] != 0:
            return True if target_piece.color == "black" else False
        elif color == "black" and self.grid[row][col] != 0:
            return True if target_piece.color == "white" else False
        return False

    def is_friend(self, position: tuple, color: str) -> bool:
        row, col = position
        target_piece = self.grid[row][col]
        if color == "white" and target_piece != 0:
            return True if target_piece.color == "white" else False
        elif color == "black" and target_piece != 0:
            return True if target_piece.color == "black" else False
        return False

    def is_valid(self, position: tuple, color: str) -> bool:
        row, col = position
        is_range = (0 <= row < 8 and 0 <= col < 8 )
        return is_range and not self.is_friend(position, color)

    def is_empty(self, position: tuple) -> bool:
        if self.grid[position[0]][position[1]] == 0:
            return True
        return False

    def count_pieces(self, color: str= None, name: str = None) -> int:
        c = 0
        for row in self.grid:
            for piece in row:
                if piece != 0:
                    if name:
                        if color and piece.color == color and piece.NAME == name:
                            c += 1
                    else:
                        if color and piece.color == color:
                            c += 1
                        elif not color:
                            c += 1
        return c

    def count_specials_pawn(self, color: str = None):
        backward = 0
        isolated = 0
        doubled = 0
        for row in self.grid:
            for piece in row:
                if piece != 0 and piece.NAME == "Pawn" and piece.color == color:
                    if piece.check_doubled(self.grid):
                        doubled += 1
                    if piece.check_backward(self.grid):
                        backward += 1
                    if piece.check_isolated(self.grid):
                        isolated += 1

        return {"backward": backward, "isolated": isolated, "doubled": doubled}

    def show_board(self):
        for row in self.grid:
            print("[", end='')
            for piece in row:
                if piece != 0 and piece.NAME == "Pawn":
                    print(f"{piece.NAME} {"W" if piece.color == "white" else "B"},  ", end='')
                else:
                    print(f"{f"{piece.NAME} {"W" if piece.color == "white" else "B"}" if piece != 0 else f"   {piece}   "}, ", end='')
            print(']')

def setup_board(list_pieces: set[Piece]) -> Board:
    board = Board()
    for piece in list_pieces:
        for position in piece.WHITE_POSITION:
            board.set_position(position, piece(color="white", position=position))

        for position in piece.BLACK_POSITION:
            board.set_position(position, piece(color="black", position=position))
    
    for row in range(len(board.grid)):
        for col in range(len(board.grid)):
            if not board.grid[row][col]:
                board.grid[row][col] = 0

    return board