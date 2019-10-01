class State:
    """
    A class used to represent a state for the n_queens problem
    """

    def __init__(self, n_queens=8, board=None, column=-1, line=-1, parent=None):
        """
        Constructor for the State class
        :param n_queens: Number of queens for the n_queens problem
        :param board: State of the parents board
        :param column: Column in which the queen will be positioned
        :param line: Line in which the queen will be positioned
        :param parent: Parent node of the state, used only for showing the path to the state
        """
        
        if board is None:
            board = []
        # Determina a quantidade de rainhas do problema
        self.n_queens = n_queens
        # Cria o vetor de tamanho n_queens que representa o tabuleiro
        self.board = [-1] * n_queens
        # Preenche o vetor com as rainhas ja posicionadas de seu pai
        for i, q in enumerate(board):
            self.board[i] = q
        # Indica em que linha e coluna será posicionada a próxima rainha
        self.column = column
        self.board[column] = line
        self.parent = parent

    def generate(self, verbose):
        """
        Generator of states for the state class
        :return: Returns the result of the Tester, and the generated states
        """
        # Guadará os estados gerados pelo estado
        generated = []
        # Se não preenchemos o vetor
        if not (self.column + 1 == self.n_queens):
            # Estes são nossos operadores, que atual da seguinte maneira
            # Adicionamos uma rainha em cada linha na ultima coluna vazia do tabuleiro
            # A ordem segue de cima para baixo
            for i in range(self.n_queens):
                generated.append(State(self.n_queens, self.board,
                                       self.column + 1, i, self))

        # Após gerar os estados, testamos o estado que esta sendo visitado
        return self.test(verbose, generated), generated

    def test(self, verbose, generated):
        """
        Tester of state for the state class
        :return: Returns if the state is valid, and if it is an objective
        """    
        # Se posicionamos alguma rainha no tabuleiro
        if self.column != -1:
            # Para cada rainha posicionada, testamos a compatibilidade com a ultima
            for c, q in enumerate(self.board[:self.column]):
                # Se alguma estiver na mesma linha da ultima, o estado é inválido
                if q == self.board[self.column]:
                    return False, False
                # Aqui testamos se alguma rainha atinge a ultima na diagonal
                delta_col = abs(c - self.column)
                delta_row = abs(q - self.board[self.column])
                if delta_col == delta_row:
                    return False, False
            # Se nenhuma rainha atinge a ultima, e se não existir mais espaço no vetor
            # Temos nosso estado objetivo
            if (self.column + 1) == self.n_queens:
                return True, True
        # Caso ainda tivermos espaço para colocar rainhas, continuaremos a busca
        return True, False

    def print_path(self):
        parents = []
        n = self
        while n.parent != None:
            parents.append(str(n.board))
            n = n.parent
        parents.reverse()
        return '->'.join(parents)
