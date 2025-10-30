from chess_pieces import King, Pawn, Rook, Knight, Bishop, Queen, Board, Piece
from board import Board, setup_board
from moves import search_for_xequemate
from search import get_minimax
from colorama import Fore, init
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
    print("\n--------------------------- Starting Chess Game ---------------------------\n")
    board: Board = setup_board(pieces)
    turn = 0
    print(f"Turn {turn} - White turn")
    board.show_board()
    print("")
    start = time.time()
    while True:
        start1 = time.time()
        result= get_minimax(board, color="white")
        result.move.piece.has_moved = True
        print(f"time spent: {time.time()-start1}")
        print(f"Chosen move: {result.move.piece.NAME} to {result.move.position}; score: {result.score}\n")
        if result.move.promotion:
            result.move.piece = Queen(color="white", position=result.move.piece.position)
        board.set_position(result.move.position, result.move.piece)
        if search_for_xequemate(board, color="white"):
            board.show_board()
            victory_message("white")
            return
        turn += 1
        print(f"Turn {turn} - Black turn")
        board.show_board()
        time.sleep(1)
        print("\n")

        start2 = time.time()
        result2 = get_minimax(board, color="black")
        result2.move.piece.has_moved = True
        print(f"time spent: {time.time()-start2}")
        print(f"Chosen move: {result2.move.piece.NAME} to {result2.move.position}; score: {result2.score}\n")
        if result2.move.promotion:
            result2.move.piece = Queen(color="black", position=result2.move.piece.position)
        board.set_position(result2.move.position, result2.move.piece)
        if search_for_xequemate(board, color="black"):
            board.show_board()
            victory_message("black")
            return
        turn += 1
        print(f"Turn {turn} - White turn")
        board.show_board()
        time.sleep(1)

    print(f"Total time spent: {time.time()-start}")

def victory_message(message):
    print(Fore.GREEN + f"\n************************* CHECK MATE, {message.upper()} WINS! *************************")


if __name__ == "__main__":
    main()
