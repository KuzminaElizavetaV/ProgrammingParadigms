import random


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board):
        pass


class HumanPlayer(Player):
    def make_move(self, board):
        available_moves = [(row + 1, col + 1) for row in range(3) for col in range(3) if board.board[row][col] == ' ']
        print(f"Доступно для хода: {available_moves} ")
        row = int(input("Введите номер строки от 1 до 3: "))
        col = int(input("Введите номер столбца от 1 до 3: "))
        return row - 1, col - 1


class ComputerPlayer(Player):
    def make_move(self, board):
        available_moves = [(row, col) for row in range(3) for col in range(3) if board.board[row][col] == ' ']
        row, col = random.choice(available_moves)
        return row, col
