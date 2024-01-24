from board import Board


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        # Создаем игровое поле
        self.board = Board()

    def play(self):
        self.board.display()
        current_player = self.player1

        while True:
            print(f"Ходит игрок {current_player.name} ({current_player.symbol})")
            move = current_player.make_move(self.board)
            moved = self.board.make_move(current_player, *move)
            self.board.display()

            if moved:
                if self.board.is_winner(current_player.symbol):
                    print(f"Игрок {current_player.name} победил!")
                    break
                elif self.board.is_full():
                    print("Ничья!")
                    break
                else:
                    current_player = self.player2 if current_player == self.player1 else self.player1
