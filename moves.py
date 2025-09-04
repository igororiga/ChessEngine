from board import Board
from chess_pieces import Piece
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