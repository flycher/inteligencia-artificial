class State:
    """
    A class used to represent a state for the n_queens problem
    """

    def __init__(self, n_queens=8, board=None, column=-1, line=-1):
        """
        Constructor for the State class
        :param n_queens: Number of queens for the n_queens problem
        :param board: State of the parents board
        :param column: Column in which the queen will be positioned
        :param line: Line in which the queen will be positioned
        """
        if board is None:
            board = []
        self.n_queens = n_queens
        self.board = [-1] * n_queens
        for i, q in enumerate(board):
            self.board[i] = q
        self.column = column
        self.board[column] = line

    def generate(self):
        """
        Generator of states for the state class
        :return: Returns the result of the Tester, and the generated states
        """
        generated = []
        if not (self.column + 1 == self.n_queens):
            for i in range(self.n_queens):
                generated.append(State(self.n_queens, self.board,
                                       self.column + 1, i))
        return self.test(), generated

    def test(self):
        """
        Tester of state for the state class
        :return: Returns if the state is valid, and if it is an objective
        """
        board = [['X' for _ in range(self.n_queens)] for _ in range(self.n_queens)]
        for c, l in enumerate(self.board):
            board[l][c] = 'Q'
        for b in board:
            print(b)
        print("\n")
        if self.column != -1:
            for c, q in enumerate(self.board[:self.column]):
                if q == self.board[self.column]:
                    return False, False
                delta_col = abs(c - self.column)
                delta_row = abs(q - self.board[self.column])
                if delta_col == delta_row:
                    return False, False
            if (self.column + 1) == self.n_queens:
                return True, True
        return True, False

