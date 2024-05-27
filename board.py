class Board:
    def __init__(self):
        self.board_state = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

    def print_board(self):
        for row in self.board_state:
            print(' | '.join(row))
            print('-' * 10)

    def make_move(self, symbol, row, col):
        if self.board_state[row][col] in ['X', 'O']:
            return False
        self.board_state[row][col] = symbol
        return True

    def has_won(self):
        for row in self.board_state:
            if all(cell == 'X' for cell in row):
                return True
            if all(cell == 'O' for cell in row):
                return True
        for col in range(3):
            if all(row[col] == 'X' for row in self.board_state):
                return True
            if all(row[col] == 'O' for row in self.board_state):
                return True
        if all(self.board_state[i][i] == 'X' for i in range(3)):
            return True
        if all(self.board_state[i][2-i] == 'X' for i in range(3)):
            return True
        if all(self.board_state[i][i] == 'O' for i in range(3)):
            return True
        if all(self.board_state[i][2-i] == 'O' for i in range(3)):
            return True
        return False