"""

Tic-Tac-Toe for two players: A valid play is a pair of coordinates in range [0, 2] separated by a space: [0 0], [0 1], [0 2], [1 0], [1 1], [1 2], [2 0] [2 1], [2 2]

"""


class TicTacToe():
    def __init__(self, board=[['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]):
        self.__board = board
        self.__player_turn = 'X'
        self.__infinity = 10

    def __show_board(self):
        print("")

        for i in range(0, 3):
            for j in range(0, 3):
                print("{}|".format(self.__board[i][j]), end="")

            print("")

        print("")

    def __valid_coordinates(self, px, py):
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        elif self.__board[px][py] != '_':
            return False
        else:
            return True

    def __game_over(self):

        # horizontal win: X player wins when ['X', 'X', 'X'] in rows 0 to 2

        for i in range(0, 3):
            if (self.__board[i] == ['X', 'X', 'X']):
                return 'X'

        # horizontal win: O player wins when ['X', 'X', 'X'] in rows 0 to 2

        for i in range(0, 3):
            if (self.__board[i] == ['O', 'O', 'O']):
                return 'O'

        # vertical win: for i=0 to 2 board positions [0][i], [1][i], and [2][i] are not '_' and have the same value

        for i in range(0, 3):
            if (self.__board[0][i] != '_' and self.__board[0][i] == self.__board[1][i] and self.__board[1][i] == self.__board[2][i]):
                return self.__board[0][i]

        # main diagonal win: board positions [0][0], [1][1], and [2][2] have the same value

        if (self.__board[0][0] != '_' and self.__board[0][0] == self.__board[1][1] and self.__board[0][0] == self.__board[2][2]):
            return self.__board[0][0]

        # second diagonal win: board positions [0][2], [1][1], and [2][0] have the same value

        if (self.__board[0][2] != '_' and self.__board[0][2] == self.__board[1][1] and self.__board[0][2] == self.__board[2][0]):
            return self.__board[0][2]

        # if the board is full the game ends with a tie

        for i in range(0, 3):
            for j in range(0, 3):
                # if there is an empty position '_', the game is not over

                if (self.__board[i][j] == '_'):
                    return None

        return '_'

    def __minimax_max(self, alpha, beta):
        max_score = -self.__infinity

        max_px = -1
        max_py = -1

        winner = self.__game_over()

        if winner == 'X':
            return (-1, 0, 0)
        elif winner == 'O':
            return (1, 0, 0)
        elif winner == '_':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.__board[i][j] == '_':
                    self.__board[i][j] = 'O'

                    (score, min_x, min_y) = self.__minimax_min(alpha, beta)

                    if score > max_score:
                        max_score = score
                        max_px = i
                        max_py = j

                    self.__board[i][j] = '_'

                    if max_score > alpha:
                        alpha = max_score

        return (max_score, max_px, max_py)

    def __minimax_min(self, alpha, beta):
        min_score = self.__infinity

        min_px = -1
        min_py = -1

        winner = self.__game_over()

        if winner == 'X':
            return (-1, 0, 0)
        elif winner == 'O':
            return (1, 0, 0)
        elif winner == '_':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.__board[i][j] == '_':
                    self.__board[i][j] = 'X'

                    (score, max_x, max_y) = self.__minimax_max(alpha, beta)

                    if score < min_score:
                        min_score = score
                        min_px = i
                        min_py = j

                    self.__board[i][j] = '_'

                    if min_score < beta:
                        beta = min_score

        return (min_score, min_px, min_py)

    def play(self):
        while True:
            self.__show_board()

            winner = self.__game_over()

            # if the game is over

            if winner != None:
                if winner == 'X':
                    print("X wins!")
                elif winner == 'O':
                    print("O wins!")
                elif winner == '_':
                    print("The game ends with a tie!")

                return

            if self.__player_turn == 'X':

                # X plays

                while True:
                    print("X plays at coordinates x y: ", end="")

                    px, py = map(int, input().split())

                    if self.__valid_coordinates(px, py):
                        self.__board[px][py] = 'X'
                        self.__player_turn = 'O'
                        break
                    else:
                        print("Coordinates are not valid! Play again")

            else:
                # O plays
                # print("O plays at coordinates x y: ", end="")

                # px, py = map(int, input().split())

                # if self.__valid_coordinates(px, py):
                #     self.__board[px][py] = 'O'
                #     self.__player_turn = 'X'
                #     break
                # else:
                #     print("Coordinates are not valid! Play again")

                (score, px, py) = self.__minimax_max(-self.__infinity, self.__infinity)

                print(
                    f"O plays at coordinates {px} {py} with a calculated score of {score}")

                self.__board[px][py] = 'O'
                self.__player_turn = 'X'
