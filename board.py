from chess_pieces import Piece
from typing import List
import time

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
    
    def count_center_pieces(self):
        center = [(3, 3), (4, 3), (3, 4), (4, 4)]
        white_pieces, black_pieces = 0, 0
        for position in center:
            x, y = position
            piece = self.grid[x][y]
            if piece != 0:
                if piece.color == "white":
                    white_pieces += 1
                elif piece.color == "black":
                    black_pieces += 1
            
        return white_pieces, black_pieces

    def count_pieces(self) -> dict:
        pieces_dict = {}
        for row in self.grid:
            for piece in row:
                if piece != 0:
                    if f"{piece.NAME}_{piece.color}" in pieces_dict:
                        pieces_dict[f"{piece.NAME}_{piece.color}"] += 1
                    else:
                        pieces_dict[f"{piece.NAME}_{piece.color}"] = 1
        return pieces_dict

    def count_specials_pawn(self) -> dict:
        backwardW, backwardB = 0, 0
        isolatedW, isolatedB = 0, 0
        doubledW, doubledB = 0, 0
        for row in self.grid:
            for piece in row:
                if piece != 0 and piece.NAME == "Pawn":
                    if piece.check_doubled(self.grid):
                        if piece.color == 'white':
                            doubledW += 1
                        else:
                            doubledB += 1
                    if piece.check_backward(self.grid):
                        if piece.color == 'white':
                            backwardW += 1
                        else:
                            backwardB += 1
                    if piece.check_isolated(self.grid):
                        if piece.color == 'white':
                            isolatedW += 1
                        else:
                            isolatedB += 1

        return {"backward": (backwardW, backwardB), "isolated": (isolatedW, isolatedB), "doubled": (doubledW, doubledB)}

    """def can_castle(self, color: str, side: str) -> bool:
        if color == "white":
            row = 0
        else:
            row = 7

        king_col = 4
        if side == "kingside":
            rook_col = 7
            path = [5, 6]
        elif side == "queenside":
            rook_col = 0
            path = [3, 2, 1]
        else:
            return False

        king = self.grid[row][king_col]
        rook = self.grid[row][rook_col]

        if (
            king == 0 or rook == 0 or
            king.NAME != "King" or rook.NAME != "Rook" or
            getattr(king, "has_moved", True) or getattr(rook, "has_moved", True)
        ):
            return False

        # Verifica se as casas entre o rei e a torre estão vazias
        for col in path:
            if self.grid[row][col] != 0:
                return False

        return True

    def can_castle_kingside(self, color: str) -> bool:
        return self.can_castle(color, "kingside")

    def can_castle_queenside(self, color: str) -> bool:
        return self.can_castle(color, "queenside")"""

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

def pawn_to_queen(position: tuple, piece: Piece, type: Piece):
    x, y = position
    if piece.NAME == "Pawn" and ((piece.color == 'white' and x == 7) or (piece.color == 'black' and x == 0)):
        return type(piece.color, piece.position)
    return piece

def is_checkmate(position: tuple, board: Board):
    x, y = position
    if board.grid[x][y] != 0 and board.grid[x][y].NAME == "King":
        return True
    return False