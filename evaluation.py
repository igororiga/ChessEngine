from board import Board
from chess_pieces import Piece
from typing import Dict, List
from dataclasses import dataclass
from moves import get_valid_moves, simulate_move, ValidMove

@dataclass(frozen=True)
class MoveEvaluation:
    move: ValidMove
    score: int = 0

def evaluation_function(board: Board) -> int:
    Qw, Qb = board.count_pieces(color='white', name='Queen'), board.count_pieces(color='black', name='Queen')
    Kw, Kb = board.count_pieces(color='white', name='King'), board.count_pieces(color='black', name='King')
    Bw, Bb = board.count_pieces(color='white', name='Bishop'), board.count_pieces(color='black', name='Bishop')
    Rw, Rb = board.count_pieces(color='white', name='Rook'), board.count_pieces(color='black', name='Rook')
    Knw, Knb = board.count_pieces(color='white', name='Knight'), board.count_pieces(color='black', name='Knight')
    Pw, Pb = board.count_pieces(color='white', name='Pawn'), board.count_pieces(color='black', name='Pawn')
    Mw, Mb = len(get_valid_moves(board, step=None, color="white")), len(get_valid_moves(board, step=None, color="black"))
    specials_pawn  = board.count_specials_pawn(color='white')
    Dw, Iw, BWw = specials_pawn["doubled"], specials_pawn["isolated"], specials_pawn["backward"]
    specials_pawn  = board.count_specials_pawn(color='black')   
    Db, Ib, BWb = specials_pawn["doubled"], specials_pawn["isolated"], specials_pawn["backward"]

    func = 200*(Kw - Kb) + 9*(Qw - Qb) + 5*(Rw - Rb) + 3*(Bw - Bb + Knw - Knb) + (Pw - Pb) + (Mw - Mb) - 5*(Dw + BWw + Iw - Db - Ib - BWb) 
    #print(Qw, Qb, Kw, Kb, Bw, Bb, Rw, Rb, Knw, Knb, Pw, Pb)
    return func

def evaluate_move(valid_move: ValidMove) -> MoveEvaluation:
    valid_score = evaluation_function(valid_move.board)
    move_eval = MoveEvaluation(move=valid_move, score=valid_score)

    return move_eval
