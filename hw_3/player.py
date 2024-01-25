import random
from colorama import init, Fore

init(autoreset=True)


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board):
        pass


class HumanPlayer(Player):
    def make_move(self, board):
        available_moves = [(row + 1, col + 1) for row in range(3) for col in range(3) if board.board[row][col] == ' ']
        print(Fore.CYAN + f"ВАРИАНТЫ ХОДА: {available_moves} ")
        row_col = input(Fore.GREEN + "\nВВЕДИТЕ НОМЕР СТРОКИ И СТОЛБЦА ЧЕРЕЗ ПРОБЕЛ: ")
        row, col = row_col.split()
        return int(row) - 1, int(col) - 1


class ComputerPlayer(Player):
    def make_move(self, board):
        available_moves = [(row, col) for row in range(3) for col in range(3) if board.board[row][col] == ' ']
        row, col = random.choice(available_moves)
        return row, col
