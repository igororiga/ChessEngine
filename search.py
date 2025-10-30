from board import Board
from chess_pieces import Queen
from evaluation import evaluate_move, MoveEvaluation
from moves import get_valid_moves
import time

"""def get_minimax(board: Board, color: str) -> MoveEvaluation:
    valid_moves = get_valid_moves(board, step=0, color=color, queen=Queen)
    first_moves_eval = []
    total_moves = 0
    # Step 1 - Team possible moviments
    alpha = None
    for move in valid_moves:
        opponent_valid_moves = get_valid_moves(move.board, step = 1, color="black" if color=="white" else "white", queen=Queen)
        opponent_moves_eval = []
        total_moves += 1

        beta = None
        # Step 2 - Opponent possible moviments
        for oppenent_move in opponent_valid_moves:
            second_valid_moves = get_valid_moves(oppenent_move.board, step = 2, color=color, queen=Queen)
            second_moves_eval = []
            total_moves += 1

            # Step 3 - Team Possible moviments
            for second_move in second_valid_moves:
                move_eval = evaluate_move(second_move)
                second_moves_eval.append(move_eval)
                total_moves += 1
                # Beta Pruning
                if not beta:
                    continue
                elif (move_eval.score >= beta and color == "white") or (move_eval.score <= beta and color == "black"):
                    break

            if color == "white":
                best_second_move = max(second_moves_eval, key=lambda move: move.score)
            else:
                best_second_move = min(second_moves_eval, key=lambda move: move.score)
            # Alpha pruning
            if not beta:
                beta = best_second_move.score
            elif (color == "white" and best_second_move.score < beta) or (color == "black" and best_second_move.score > beta):
                beta = best_second_move.score
            opponent_moves_eval.append(MoveEvaluation(move=oppenent_move, score=best_second_move.score))
            if not alpha:
                pass
            elif (best_second_move.score <= alpha and color == "white") or (best_second_move.score >= alpha and color == "black"):
                break

        if color == "white":
            best_opponent_move = min(opponent_moves_eval, key=lambda move: move.score)
        else:
            best_opponent_move = max(opponent_moves_eval, key=lambda move: move.score)

        # Set the best score for pruning
        if not alpha:
            alpha = best_opponent_move.score
        elif (color == "white" and best_opponent_move.score > alpha) or (color == "black" and best_opponent_move.score < alpha):
            alpha = best_opponent_move.score
        #best_opponent_move.move.board.show_board()
        first_moves_eval.append(MoveEvaluation(move=move, score=best_opponent_move.score))

    if color == "white":
        best_move = max(first_moves_eval, key=lambda move_eval: move_eval.score)
    else:
        best_move = min(first_moves_eval, key=lambda move_eval: move_eval.score)

    #print(best_move.move.board.show_board())
    print(f"Total moves evaluated: {total_moves}")
    return best_move"""

"""def get_minimax(board: Board, color: str) -> MoveEvaluation:
    valid_moves = get_valid_moves(board, step=0, color=color, queen=Queen)
    first_moves_eval = []
    total_moves = 0
    # Step 1 - Team possible moviments
    alpha = None
    for move in valid_moves:
        opponent_valid_moves = get_valid_moves(move.board, step = 1, color="black" if color=="white" else "white", queen=Queen)
        opponent_moves_eval = []
        total_moves += 1

        # Step 2 - Opponent possible moviments
        for oppenent_move in opponent_valid_moves:
            move_eval = evaluate_move(oppenent_move)
            opponent_moves_eval.append(move_eval)
            total_moves += 1
            # Alpha Pruning
            if not alpha:
                continue
            if (move_eval.score <= alpha and color == "white") or (move_eval.score >= alpha and color == "black"):
                break

        if color == "white":
            best_opponent_move = min(opponent_moves_eval, key=lambda move: move.score)
        else:
            best_opponent_move = max(opponent_moves_eval, key=lambda move: move.score)

        # Set the best score for pruning
        if not alpha:
            alpha = best_opponent_move.score 
        elif (color == "white" and best_opponent_move.score > alpha) or (color == "black" and best_opponent_move.score < alpha):
            alpha = best_opponent_move.score
        #best_opponent_move.move.board.show_board()
        first_moves_eval.append(MoveEvaluation(move=move, score=best_opponent_move.score))

    if color == "white":
        best_move = max(first_moves_eval, key=lambda move_eval: move_eval.score)
    else:
        best_move = min(first_moves_eval, key=lambda move_eval: move_eval.score)

    #print(best_move.move.board.show_board())
    print(f"Total moves evaluated: {total_moves}")
    return best_move"""

def get_minimax(board: Board, color: str) -> MoveEvaluation:
    valid_moves = get_valid_moves(board, step=0, color=color, queen=Queen)
    if not valid_moves:
        print("Total moves evaluated: 0")
        return None
    moves_eval = []
    for move in valid_moves:
        mv_eval = evaluate_move(move)
        moves_eval.append(MoveEvaluation(move=move, score=mv_eval.score))

    if color == "white":
        best_move = max(moves_eval, key=lambda m: m.score)
    else:
        best_move = min(moves_eval, key=lambda m: m.score)

    print(f"Total moves evaluated: {len(moves_eval)}")
    return best_move

