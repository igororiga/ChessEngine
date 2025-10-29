from board import Board, pawn_to_queen
from chess_pieces import Piece, Queen
from copy import deepcopy
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class ValidMove:
    piece: Piece
    position: tuple
    board: Board
    step: int

def simulate_move(board: Board, piece: Piece, move: tuple) -> Board:
    new_board = Board()
    new_board.grid = deepcopy(board.grid)
    piece = pawn_to_queen(position=move, piece=piece, type=Queen)  # Just to check for promotion
    new_board.set_position(move, piece, update_position=False)

    return new_board

def get_valid_moves(board: Board, step: int, color: str = None) -> List[ValidMove]:
    all_moves = []
    for row in board.grid:
        for piece in row:
            # Checks for not empty places and matching color
            if piece != 0 and color == piece.color:
                valid_moves = piece.check_valid_moves(board)
                valid_moves = [ValidMove(piece=piece, position=move, board=simulate_move(board, piece, move), step=step) for move in valid_moves]
                all_moves.append(valid_moves)

    all_moves = [move for list_move in all_moves for move in list_move]  # Flat list
    return all_moves

def search_for_xequemate(board: Board, color: str) -> bool:
    for row in board.grid:
        for piece in row:
            if piece != 0 and color == piece.color:
                mate_position = is_mate(board, piece)
                if mate_position:
                    x, y = mate_position
                    if is_xequemate(board, x, y):
                        return True
            elif piece != 0 and color != piece.color:
                mate_position = is_mate(board, piece)
                if mate_position:
                    return True
    return False

def is_mate(board: Board, piece: Piece) -> bool:
    valid_moves = piece.check_valid_moves(board)
    for move in valid_moves:
        x, y = move
        if board.grid[x][y] != 0 and board.grid[x][y].NAME == "King" and board.grid[x][y].color != piece.color:
            return (x, y)
    return False
                    
def is_xequemate(board: Board, x, y) -> bool:
    king = board.grid[x][y]
    valid_moves = king.check_valid_moves(board)
    for move in valid_moves:
        new_board = simulate_move(board, king, move)
        for row in new_board.grid:
            for piece in row:
                if piece != 0 and king.color != piece.color:
                    return is_mate(board, piece)
    return False