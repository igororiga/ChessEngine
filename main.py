from chess_pieces import King, Pawn, Rook, Knight, Bishop, Queen, Board, Piece
from board import Board, setup_board, pawn_to_queen, is_checkmate
from search import get_minimax
from colorama import Fore, Style, init
import time

init(autoreset=True)
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
    turn = 0
    print(f"Turn {turn} - White turn")
    board.show_board()
    print("")
    while True:
        start1 = time.time()
        result= get_minimax(board, color="white")
        result.move.piece = pawn_to_queen(result.move.position, result.move.piece, Queen)
        if is_checkmate(result.move.position, board):
            board.set_position(result.move.position, result.move.piece)
            board.show_board()
            victory_message("white")
            return
        board.set_position(result.move.position, result.move.piece)
        print(f"time spent: {time.time()-start1}")
        print(f"Turn {turn} - Black turn")
        board.show_board()
        print("\n")

        start2 = time.time()
        result2 = get_minimax(board, color="black")
        result2.move.piece = pawn_to_queen(result2.move.position, result2.move.piece, Queen)
        if is_checkmate(result2.move.position, board):
            board.set_position(result2.move.position, result2.move.piece)
            board.show_board()
            victory_message("black")
            return
        board.set_position(result2.move.position, result2.move.piece)
        turn += 1
        print(f"time spent: {time.time()-start2}")
        print(f"Turn {turn} - White turn")
        board.show_board()
        print("\n")

def victory_message(message):
    print(Fore.GREEN + f"\n*********************** CHECK MATE, {message.upper()} WINS! ***********************")


if __name__ == "__main__":
    main()
