from search.BlindSearch import BlindSearch
from search.structures.Queue import Queue


class BFS(BlindSearch):
    """
    A class representing an implementation for a
    Breadth First Search algorithm for the N Queens problem
    """

    def __init__(self, n_queens=8):
        """
        :param n_queens: The size of the board for the problem
        """
        super().__init__(n_queens)
        self.structure = Queue()
