import random


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board):
        pass


class HumanPlayer(Player):
    def make_move(self, board):
        available_moves = [(row, col) for row in range(3) for col in range(3) if board.board[row][col] == ' ']
        print(f"Доступно для хода: {available_moves} ")
        row = int(input("Введите номер строки от 0 до 2: "))
        col = int(input("Введите номер столбца от 0 до 2: "))
        return row, col


class ComputerPlayer(Player):
    def make_move(self, board):
        available_moves = [(row, col) for row in range(3) for col in range(3) if board.board[row][col] == ' ']
        row, col = random.choice(available_moves)
        return row, col
