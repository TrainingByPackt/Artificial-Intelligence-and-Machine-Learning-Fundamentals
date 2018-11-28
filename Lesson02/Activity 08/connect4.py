from easyAI import TwoPlayersGame
from easyAI.Player import Human_Player


class ConnectFour(TwoPlayersGame):
    def __init__(self, players):
        self.players = players
        #  0  1  2  3  4  5  6
        #  7  8  9 10 11 12 13
        # ...
        # 35 36 37 38 39 40 41
        self.board = [0 for i in range(42)]
        self.nplayer = 1  # player 1 starts.

        def generate_winning_tuples():
            tuples = []
            # horizontal
            tuples += [
                list(range(row*7+column, row*7+column+4, 1))
                for row in range(6)
                for column in range(4)
            ]
            # vertical
            tuples += [
                list(range(row*7+column, row*7+column+28, 7))
                for row in range(3)
                for column in range(7)
            ]
            # diagonal forward
            tuples += [
                list(range(row*7+column, row*7+column+32, 8))
                for row in range(3)
                for column in range(4)
            ]
            # diagonal backward
            tuples += [
                list(range(row*7+column, row*7+column+24, 6))
                for row in range(3)
                for column in range(3, 7, 1)
            ]
            return tuples
        self.tuples = generate_winning_tuples()

    def possible_moves(self):
        return [column+1
                for column in range(7)
                if any([
                    self.board[column+row*7] == 0
                    for row in range(6)
                ])
                ]

    def make_move(self, move):
        column = int(move) - 1
        for row in range(5, -1, -1):
            index = column + row*7
            if self.board[index] == 0:
                self.board[index] = self.nplayer
                return

    def unmake_move(self, move):  # optional method (speeds up the AI)
        column = int(move) - 1
        for row in range(6):
            index = column + row*7
            if self.board[index] != 0:
                self.board[index] = 0
                return

    def lose(self):
        return any([all([(self.board[c] == self.nopponent)
                         for c in line])
                    for line in self.tuples])

    def is_over(self):
        return (self.possible_moves() == []) or self.lose()

    def show(self):
        print('\n'+'\n'.join([
            ' '.join([['.', 'O', 'X'][self.board[7*row+column]]
                      for column in range(7)]
                     )
            for row in range(6)])
        )

    def scoring(self):
        return -100 if self.lose() else 0


if __name__ == "__main__":
    from easyAI import AI_Player, Negamax
    ai_algo = Negamax(6)
    ConnectFour([Human_Player(), AI_Player(ai_algo)]).play()
