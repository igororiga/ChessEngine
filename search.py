from board import Board
from evaluation import evaluate_move, MoveEvaluation
from moves import get_valid_moves
import time

"""def get_minimax(board: Board, color: str) -> MoveEvaluation:
    valid_moves = get_valid_moves(board, step=0, color=color)
    first_moves_eval = []
    total_moves = 0
    # Step 1 - Team possible moviments
    for move in valid_moves:
        opponent_valid_moves = get_valid_moves(move.board, step = 1, color="black" if color=="white" else "white")
        opponent_moves_eval = []

        # Step 2 - Opponent possible moviments
        for oppenent_move in opponent_valid_moves:
            second_valid_moves = get_valid_moves(oppenent_move.board, step = 2, color=color)
            second_moves_eval = []
            # Step 3 - Team Possible moviments
            for second_move in second_valid_moves:
                move_eval = evaluate_move(second_move)
                second_moves_eval.append(move_eval)
                total_moves += len(second_valid_moves)
            
            if color == "white":
                best_second_move = max(second_moves_eval, key=lambda move: move.score)
            else:
                best_second_move = min(second_moves_eval, key=lambda move: move.score)
            opponent_moves_eval.append(MoveEvaluation(move=oppenent_move, score=best_second_move.score))

        if color == "white":
            best_opponent_move = min(opponent_moves_eval, key=lambda move: move.score)
        else:
            best_opponent_move = max(opponent_moves_eval, key=lambda move: move.score)
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
    valid_moves = get_valid_moves(board, step=0, color=color)
    first_moves_eval = []
    total_moves = 0
    # Step 1 - Team possible moviments
    best_score = None
    for move in valid_moves:
        opponent_valid_moves = get_valid_moves(move.board, step = 1, color="black" if color=="white" else "white")
        opponent_moves_eval = []

        # Step 2 - Opponent possible moviments
        for oppenent_move in opponent_valid_moves:
            move_eval = evaluate_move(oppenent_move)
            opponent_moves_eval.append(move_eval)
            total_moves += len(opponent_moves_eval)
            # Alpha-Beta Pruning
            if not best_score:
                continue
            if (move_eval.score <= best_score and color == "white") or (move_eval.score >= best_score and color == "black"):
                break

        if color == "white":
            best_opponent_move = min(opponent_moves_eval, key=lambda move: move.score)
        else:
            best_opponent_move = max(opponent_moves_eval, key=lambda move: move.score)

        # Set the best score for pruning
        if not best_score:
            best_score = best_opponent_move.score 
        elif (color == "white" and best_opponent_move.score > best_score) or (color == "black" and best_opponent_move.score < best_score):
            best_score = best_opponent_move.score
        #best_opponent_move.move.board.show_board()
        first_moves_eval.append(MoveEvaluation(move=move, score=best_opponent_move.score))

    if color == "white":
        best_move = max(first_moves_eval, key=lambda move_eval: move_eval.score)
    else:
        best_move = min(first_moves_eval, key=lambda move_eval: move_eval.score)

    #print(best_move.move.board.show_board())
    print(f"Total moves evaluated: {total_moves}")
    return best_move