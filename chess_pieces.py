from typing import List
import abc

class Piece:
    NAME: str
    WHITE_POSITION: List[tuple]
    BLACK_POSITION: List[tuple]
    VALUE: int

    def __init__(self, color, position):
        self.color = color
        self.position = position

from board import Board

class King(Piece):
    NAME: str = "King"
    WHITE_POSITION: List[tuple] = [(0, 4)]
    BLACK_POSITION: List[tuple] = [(7, 4)]
    VALUE: int = 6

    def check_valid_moves(self, board: Board) -> List:
        moves = []
        row, col = self.position
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1), (1, 0), (1, 1)]
        for move in directions:
            new_row, new_col = row + move[0], col + move[1]
            if board.is_valid((new_row, new_col), self.color):
                moves.append((new_row, new_col))

        return moves

class Queen(Piece):
    NAME: str = "Queen"
    WHITE_POSITION: List[tuple] = [(0, 3)]
    BLACK_POSITION: List[tuple] = [(7, 3)]
    VALUE: int = 5

    def check_valid_moves(self, board: Board) -> List:
        moves = []
        row, col = self.position

        for x in range(row+1, 8):
            if board.is_enemy((x, col), self.color):
                moves.append((x, col))
                break
            elif board.is_valid((x, col), self.color):
                moves.append((x, col))
            else:
                break
        
        for x in range(row-1, -1, -1):
            if board.is_enemy((x, col), self.color):
                moves.append((x, col))
                break
            elif board.is_valid((x, col), self.color):
                moves.append((x, col))
            else:
                break
        
        for y in range(col+1, 8):
            if board.is_enemy((row, y), self.color):
                moves.append((row, y))
                break
            elif board.is_valid((row, y), self.color):
                moves.append((row, y))
            else:
                break
        
        for y in range(col-1, -1, -1):
            if board.is_enemy((row, y), self.color):
                moves.append((row, y))
                break
            elif board.is_valid((row, y), self.color):
                moves.append((row, y))
            else:
                break

        for d in range(1, 8):
            if board.is_valid((row+d, col+d), self.color) and board.is_enemy((row+d, col+d), self.color):
                moves.append((row + d, col + d))
                break
            elif board.is_valid((row+d, col+d), self.color):
                moves.append((row + d, col + d))
            else:
                break

        for d in range(1, 8):
            if board.is_valid((row+d, col-d), self.color) and board.is_enemy((row+d, col-d), self.color):
                moves.append((row + d, col - d))
                break
            elif board.is_valid((row+d, col-d), self.color):
                moves.append((row + d, col - d))
            else:
                break
        
        for d in range(1, 8):
            if board.is_valid((row-d, col+d), self.color) and board.is_enemy((row-d, col+d), self.color):
                moves.append((row - d, col + d))
                break
            elif board.is_valid((row-d, col+d), self.color):
                moves.append((row - d, col + d))
            else:
                break
        
        for d in range(1, 8):
            if board.is_valid((row-d, col-d), self.color) and board.is_enemy((row-d, col-d), self.color):
                moves.append((row - d, col - d))
                break
            elif board.is_valid((row-d, col-d), self.color):
                moves.append((row - d, col - d))
            else:
                break

        return moves

class Rook(Piece):
    NAME: str = "Rook"
    WHITE_POSITION: List[tuple] = [(0, 0), (0, 7)]
    BLACK_POSITION: List[tuple] = [(7, 0), (7, 7)]
    VALUE: int = 4

    def check_valid_moves(self, board: Board) -> List:
        moves = []
        row, col = self.position
        
        for x in range(row+1, 8):
            if board.is_enemy((x, col), self.color):
                moves.append((x, col))
                break
            elif board.is_valid((x, col), self.color):
                moves.append((x, col))
            else:
                break
        
        for x in range(row-1, -1, -1):
            if board.is_enemy((x, col), self.color):
                moves.append((x, col))
                break
            elif board.is_valid((x, col), self.color):
                moves.append((x, col))
            else:
                break
        
        for y in range(col+1, 8):
            if board.is_enemy((row, y), self.color):
                moves.append((row, y))
                break
            elif board.is_valid((row, y), self.color):
                moves.append((row, y))
            else:
                break
        
        for y in range(col-1, -1, -1):
            if board.is_enemy((row, y), self.color):
                moves.append((row, y))
                break
            elif board.is_valid((row, y), self.color):
                moves.append((row, y))
            else:
                break
                
        return moves

class Bishop(Piece):
    NAME: str = "Bishop"
    WHITE_POSITION: List[tuple] = [(0, 2), (0, 5)]
    BLACK_POSITION: List[tuple] = [(7, 2), (7, 5)]
    VALUE: int = 3

    def check_valid_moves(self, board: Board) -> List:
        moves = []
        row, col = self.position
        for d in range(1, 8):
            if board.is_valid((row+d, col+d), self.color) and board.is_enemy((row+d, col+d), self.color):
                moves.append((row + d, col + d))
                break
            elif board.is_valid((row+d, col+d), self.color):
                moves.append((row + d, col + d))
            else:
                break

        for d in range(1, 8):
            if board.is_valid((row+d, col-d), self.color) and board.is_enemy((row+d, col-d), self.color):
                moves.append((row + d, col - d))
                break
            elif board.is_valid((row+d, col-d), self.color):
                moves.append((row + d, col - d))
            else:
                break
        
        for d in range(1, 8):
            if board.is_valid((row-d, col+d), self.color) and board.is_enemy((row-d, col+d), self.color):
                moves.append((row - d, col + d))
                break
            elif board.is_valid((row-d, col+d), self.color):
                moves.append((row - d, col + d))
            else:
                break
        
        for d in range(1, 8):
            if board.is_valid((row-d, col-d), self.color) and board.is_enemy((row-d, col-d), self.color):
                moves.append((row - d, col - d))
                break
            elif board.is_valid((row-d, col-d), self.color):
                moves.append((row - d, col - d))
            else:
                break

        return moves

class Knight(Piece):
    NAME: str = "Knight"
    WHITE_POSITION: List[tuple] = [(0, 1), (0, 6)]
    BLACK_POSITION: List[tuple] = [(7, 1), (7, 6)]
    VALUE: int = 2

    def check_valid_moves(self, board: Board) -> List:
        moves = []
        row, col = self.position
        knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                        (1, -2), (1, 2), (2, -1), (2, 1)]
        for move in knight_moves:
            x, y = row + move[0], col + move[1]
            if board.is_valid((x, y), self.color):
                moves.append((x, y))

        return moves


class Pawn(Piece):
    NAME: str = "Pawn"
    WHITE_POSITION: List[tuple] = [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)]
    BLACK_POSITION: List[tuple] = [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7)]
    WHITE_ATK_MOVES: List[tuple] = [(1, 1), (1, -1)]
    BLACK_ATK_MOVES: List[tuple] = [(-1, 1), (-1, -1)]
    VALUE: int = 1

    def check_valid_moves(self, board: Board) -> List:
        moves = []
        row, col = self.position
        if self.color == "white":
            if board.is_valid((row + 1, col), self.color) and not board.is_enemy((row + 1, col), self.color):
                moves.append((row + 1, col))
            if row == 1:
                if board.is_empty((row + 1, col)) and board.is_valid((row + 2, col), self.color) and not board.is_enemy((row + 1, col), self.color):
                    moves.append((row + 2, col))
            
            for move in self.WHITE_ATK_MOVES:
                if board.is_valid(move, self.color) and board.is_enemy(move, self.color):
                    moves.append(move)

    
        if self.color == "black":
            if board.is_valid((row - 1, col), self.color) and not board.is_enemy((row - 1, col), self.color):
                moves.append((row - 1, col))
            if row == 6:
                if board.is_empty((row - 1, col)) and board.is_valid((row - 2, col), self.color) and not board.is_enemy((row - 1, col), self.color):
                    moves.append((row - 2, col))
            
            for move in self.BLACK_ATK_MOVES:
                if board.is_valid(move, self.color) and board.is_enemy(move, self.color):
                    moves.append(move)

        return moves