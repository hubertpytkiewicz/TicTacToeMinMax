from player import HumanPlayer, RandomPlayer, MinMaxPlayer
import os

class Game:
    def __init__(self, option) -> None:
        self.choose_player(option)
        self.board = [" " for i in range(9)]
        
    def print_board(self) -> None:
        for i in range(0, 7, 3):
            print(f"| {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} |\n")

    def print_instruction(self) -> None:
        print("Grid numbering: ")
        for i in range(0, 7, 3):
            print(f"| {i} | {i+1} | {i+2} |\n")
    
    def choose_player(self, option):
        if option == "rva":
            self.your_player = RandomPlayer("X")
            self.enemy_player = MinMaxPlayer("O") 
        elif option == "hva":
            self.your_player = HumanPlayer(input("What's your sign? (X or O) "))
            self.enemy_player = MinMaxPlayer("X" if self.your_player.marker == "O" else "O") 
        elif option == "hvr":
            self.your_player = HumanPlayer(input("What's your sign? (X or O) "))
            self.enemy_player = RandomPlayer("X" if self.your_player.marker == "O" else "O") 
    
    def game_loop(self) -> str:
        print("Welcome to the game!")
        self.print_instruction()

        current_player = "X"
        os.system("clear")

        while self.your_player.is_winner(self.board) == " " and " " in self.board:
            self.print_board()
            if current_player is self.your_player.marker:
                self.your_player.mark(self.board)
            else:
                self.enemy_player.mark(self.board)
            current_player = "X" if current_player == "O" else "O"
            os.system("clear")

        self.print_board()
        if self.your_player.is_winner(self.board) == "Tie":
            print("Tie...")
            return "Tie"
        else:
            print(f"AAAND THE WINNER IS: {self.your_player.is_winner(self.board)}")       
            return self.your_player.is_winner(self.board)