import random

class Player:
    def __init__(self, marker: str) -> None:
        self.marker = marker
    
    def mark(self, board: list[str]) -> bool:
        pass

class HumanPlayer(Player):
    def __init__(self, marker: str) -> None:
        super().__init__(marker)
        print(self.marker)

    def mark(self, board: list[str]) -> None:
        while True:
            pos = int(input("What's your input? (0-8) "))
            if board[pos] == " ":
                board[pos] = self.marker
                break

class RandomPlayer(Player):
    def __init__(self, marker: str) -> None:
        super().__init__(marker)

    def mark(self, board: list[str]) -> bool:
        while True:
            pos = random.randint(0,8)
            if board[pos] == " ":
                board[pos] = self.marker
                break
