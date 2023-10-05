from player import HumanPlayer, RandomPlayer
import os
import time

class Game:
    def __init__(self) -> None:
        self.choose_player()
        self.board = [" " for i in range(9)]

    def print_board(self) -> None:
        for i in range(0, 7, 3):
            print(f"| {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} |\n")

    def print_instruction(self) -> None:
        print("Grid numbering: ")
        for i in range(0, 7, 3):
            print(f"| {i} | {i+1} | {i+2} |\n")

    def get_board(self) -> list[str]:
        return self.board
    
    def choose_player(self):
        self.your_player = HumanPlayer(input("What is your player? (X or O) "))
        self.enemy_player = RandomPlayer("O" if self.your_player.marker == "X" else "X")

    def is_winner(self) -> str:
        if self.board[0] is self.board[4] is self.board[8] and " " not in {self.board[0], self.board[4], self.board[8]}:
            return self.board[4]
        
        elif self.board[2] is self.board[4] is self.board[6] and " " not in {self.board[2], self.board[4], self.board[6]}:
            return self.board[4]
        
        for i in range(0, 7, 3):
            if self.board[i] is self.board[i+1] is self.board[i+2] and " " not in {self.board[i], self.board[i+1], self.board[i+2]}:
                return self.board[i]
            if self.board[(i//3)] is self.board[(i//3)+3] is self.board[(i//3)+6] and " " not in {self.board[(i//3)], self.board[(i//3)+3], self.board[(i//3)+6]}:
                return self.board[i//3]
        return " "
    
    def game_loop(self) -> None:
        print("Welcome to the game!")
        self.print_instruction()
        current_player = "X"
        time.sleep(3)
        os.system("clear")
        while self.is_winner() == " " and " " in self.board:
            self.print_board()
            if current_player is self.your_player.marker:
                self.your_player.mark(self.get_board())
            else:
                time.sleep(1)
                self.enemy_player.mark(self.get_board())
            current_player = "X" if current_player == "O" else "O"
            os.system("clear")
        self.print_board()
        if self.is_winner() == " " and " " not in self.board:
            print("Tie...")
        else:
            print(f"AAAND THE WINNER IS: {self.is_winner()}")       