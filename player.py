import random
import math

class Player:
    def __init__(self, marker: str) -> None:
        self.marker = marker
    
    def mark(self, board: list[str]) -> None:
        pass
    
    def is_winner(self, board: list[str]) -> str:
        if board[0] is board[4] is board[8] and " " not in {board[0], board[4], board[8]}:
            return board[4]
        
        elif board[2] is board[4] is board[6] and " " not in {board[2], board[4], board[6]}:
            return board[4]
        
        for i in range(0, 7, 3):
            if board[i] is board[i+1] is board[i+2] and " " not in {board[i], board[i+1], board[i+2]}:
                return board[i]
            
            if board[(i//3)] is board[(i//3)+3] is board[(i//3)+6] and " " not in {board[(i//3)], board[(i//3)+3], board[(i//3)+6]}:
                return board[i//3]
            
        if " " not in board:
            return "Tie"
        return " "

class HumanPlayer(Player):
    def __init__(self, marker: str) -> None:
        super().__init__(marker)

    def mark(self, board: list[str]) -> None:
        while True:
            pos = int(input("What's your input? (0-8) "))
            if board[pos] == " ":
                board[pos] = self.marker
                break

class RandomPlayer(Player):
    def __init__(self, marker: str) -> None:
        super().__init__(marker)

    def mark(self, board: list[str]) -> None:
        while True:
            pos = random.randint(0,8)
            if board[pos] == " ":
                board[pos] = self.marker
                break

class MinMaxPlayer(Player):
    def __init__(self, marker: str) -> None:
        super().__init__(marker)
    
    def mark(self, board: list[str]) -> None:
        best = -math.inf
        next_move = -1
        for pos in range(0,9):
            if board[pos] == " ":
                board[pos] = self.marker
                score = self.min_max(board, False, 1)
                if score > best:
                    next_move = pos
                    best = score
                board[pos] = " "
        board[next_move] = self.marker

    def min_max(self, board: list[str], isMaximazing: bool, depth: int) -> int:
        enemy = "X" if self.marker == "O" else "O"
        if self.is_winner(board) == self.marker:
            return 1/depth
        elif self.is_winner(board) == "Tie":
            return 0
        elif self.is_winner(board) == enemy: 
            return -1/depth
        
        if isMaximazing:
            best = -math.inf
            for pos in range(0, 9):
                if board[pos] == " ":
                    board[pos] = self.marker
                    best = max(best, self.min_max(board, not isMaximazing, depth+1))
                    board[pos] = " "
            return best
        else:
            worst = math.inf
            for pos in range(0, 9):
                if board[pos] == " ":
                    board[pos] = enemy
                    worst = min(worst, self.min_max(board, not isMaximazing, depth+1))
                    board[pos] = " "
            return worst