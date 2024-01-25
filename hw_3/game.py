from board import Board
from colorama import init, Fore

init(autoreset=True)


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
            print(Fore.BLUE + f"\nХОДИТ:  {current_player.name} ({current_player.symbol})")
            move = current_player.make_move(self.board)
            moved = self.board.make_move(current_player, *move)
            self.board.display()

            if moved:
                if self.board.is_winner(current_player.symbol):
                    print(Fore.LIGHTRED_EX + f"\n{current_player.name} ВЫИГРАЛ!")
                    break
                elif self.board.is_full():
                    print(Fore.LIGHTRED_EX + "НИЧЬЯ!")
                    break
                else:
                    current_player = self.player2 if current_player == self.player1 else self.player1
