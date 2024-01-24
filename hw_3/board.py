class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def is_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def is_winner(self, symbol):
        for row in self.board:
            if row.count(symbol) == 3:
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == symbol:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == symbol:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == symbol:
            return True
        return False

    def display(self):
        print('──╂───╂──')
        for row in self.board:
            print(' ┃ '.join(row))
            print('──╂───╂──')

    def make_move(self, player, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = player.symbol
            return True
        else:
            print("Неверный ход!")
            return False
