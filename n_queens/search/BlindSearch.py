from search.State import State
from time import time


class BlindSearch:
    """
    A class representing an implementation for a
    Blind Search algorithm for the N Queens problem
    """

    def __init__(self, n_queens=8):
        """
        :param n_queens: The size of the board for the problem
        """
        self.structure = None
        self.n_queens = n_queens

    def search(self, verbose):
        """
        Executes the dfs search for the problem solution
        :return: The state with the solution for the problem,
            the number of iterations and the execution time
        """
        start = time()
        state = State(n_queens=self.n_queens)
        # Coloca o estado inicial, com nenhuma rainha no tabuleiro, e inicia a busca
        self.structure.put(state)
        iterations = 0
        # Removemos de nossa estrutura enquanto existe algo nela
        while self.structure.peek() is not None:
            iterations += 1
            state = self.structure.get()
            # Aqui geramos e testamos estado removido da estrutura
            (valid, objective), generated = state.generate(verbose)
            # Se o estado for objetivo, encerramos a busca
            if objective:
                return state, iterations, time() - start
            # Caso contrario, adicionamos os estados gerados a estrutura
            if valid:
                # Como um movimento do problema permite apenas adicionar ao tabuleiro
                # Não é necessário controle de redundância
                for st in generated:
                    self.structure.put(st)
        # Se a estrutura fica vazia e nenhum estado objetivo foi encontrado
        return None, iterations, time() - start

    def solve(self, verbose):
        """
        Prints the execution time, the number of iterations and the board with the solution
        """
        state, iterations, exec_time = self.search(verbose)
        print('Final state:')
        board = [['X' for _ in range(self.n_queens)] for _ in range(self.n_queens)]
        if state is not None:
            for c, l in enumerate(state.board):
                board[l][c] = 'Q'
        print('Search finished in {} seconds after {} iterations:'.format(exec_time, iterations))
        for b in board:
            print(b)
