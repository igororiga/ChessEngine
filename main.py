from chess_pieces import King, Pawn, Rook, Knight, Bishop, Queen, Board, Piece
from board import Board, setup_board
from evaluation import evaluation_function, evaluate_move, MoveEvaluation
from moves import get_valid_moves
from search import get_minimax
import time

initial_table = [[4, 2, 3, 5, 6, 3, 2, 4],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [-1, -1, -1, -1, -1, -1, -1, -1],
                [-4, -2, -3, -5, -6, -3, -2, -4]]

pieces = {King, Queen, Rook, Bishop, Knight, Pawn}

def main():
    board: Board = setup_board(pieces)
    #board.set_position((3, 3), board.grid[1][3], True)
    turn = 0
    print(f"Turn {turn} - White turn")
    board.show_board()
    print("")
    while True:
        start1 = time.time()
        result= get_minimax(board, color="white")
        board.set_position(result.move.position, result.move.piece)
        print(f"time spent: {time.time()-start1}")
        print(f"Turn {turn} - Black turn")
        board.show_board()
        print("\n")
        start2 = time.time()
        result2 = get_minimax(board, color="black")
        board.set_position(result2.move.position, result2.move.piece)

        turn += 1
        print(f"time spent: {time.time()-start2}")
        print(f"Turn {turn} - White turn")
        board.show_board()
        print("\n")

if __name__ == "__main__":
    main()
