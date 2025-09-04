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
    pieces_dict = board.count_pieces()
    Qw, Qb = pieces_dict.get('Queen_white', 0), pieces_dict.get('Queen_black', 0)
    Kw, Kb = pieces_dict.get('King_white', 0), pieces_dict.get('King_black', 0)
    Bw, Bb = pieces_dict.get('Bishop_white', 0), pieces_dict.get('Bishop_black', 0)
    Rw, Rb = pieces_dict.get('Rook_white', 0), pieces_dict.get('Rook_black', 0)
    Knw, Knb = pieces_dict.get('Knight_white', 0), pieces_dict.get('Knight_black', 0)
    Pw, Pb = pieces_dict.get('Pawn_white', 0), pieces_dict.get('Pawn_black', 0)
    Mw, Mb = len(get_valid_moves(board, step=None, color="white")), len(get_valid_moves(board, step=None, color="black"))
    specials_pawn  = board.count_specials_pawn()
    Dw, Db, = specials_pawn["doubled"]
    Iw, Ib = specials_pawn["isolated"]
    BWw, BWb = specials_pawn["backward"]
    func = 200*(Kw - Kb) + 9*(Qw - Qb) + 5*(Rw - Rb) + 3*(Bw - Bb + Knw - Knb) + (Pw - Pb) + (Mw - Mb) - 5*(Dw + BWw + Iw - Db - Ib - BWb) 
    #print(Qw, Qb, Kw, Kb, Bw, Bb, Rw, Rb, Knw, Knb, Pw, Pb)
    return func

def evaluate_move(valid_move: ValidMove) -> MoveEvaluation:
    valid_score = evaluation_function(valid_move.board)
    move_eval = MoveEvaluation(move=valid_move, score=valid_score)

    return move_eval
