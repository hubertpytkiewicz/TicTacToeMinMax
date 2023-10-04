import random

class Game:
    def __init__(self) -> None:
        self.choose_player()
        self.board = [" " for i in range(9)]

    def print_board(self) -> None:
        for i in range(0, 7, 3):
            print(f"| {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} |\n")

    def get_board(self) -> None:
        return self.board
    
    def choose_player(self, your_player="X"):
        self.your_player = input("What is your player? (X or O) ")
        self.enemy_player = "O" if self.your_player == "X" else "X"

    def mark(self, player: str, position: int) -> bool:
        if self.board[position] == " ":
            self.board[position] = player
            return True
        else:
            return False

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
        current_player = "X"

        while self.is_winner() == " " and " " in self.board:
            if current_player is self.your_player:
                while True:
                    pos = int(input("Your position? "))
                    if self.mark(current_player, pos):
                        break
            else:
                while True:
                    pos = random.randint(0,8)
                    if self.mark(current_player, pos):
                        break
            current_player = "X" if current_player == "O" else "O"
            self.print_board()
            
        print(f"AAAND THE WINNER ISSSSS: {self.is_winner()}")