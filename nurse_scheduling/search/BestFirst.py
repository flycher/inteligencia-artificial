from search.SchedulingProblemSearch import SchedulingProblemSearch
from search.State import State
import heapq


class BestFirst(SchedulingProblemSearch):
    """
    A class for executing the Best First Search for the scheduling problem
    """

    def __init__(self, n_nurses=10, n_periods=3, restriction_weights=None):
        if restriction_weights is None:
            restriction_weights = [1, 1, 1, 1]
        super().__init__(n_nurses, n_periods, restriction_weights)
        # Para o melhor primeiro, usamos um heap para guardar os estados gerados
        self.heap = []

    def search(self, scheduling):
        best_state = State(self.n_nurses, self.n_periods, scheduling)
        heapq.heappush(self.heap, best_state)
        iterations = 1000
        while self.heap and iterations:
            state = heapq.heappop(self.heap)
            # Guarda o melhor estado encontrado ate o momento
            if state < best_state:
                best_state = state
            print(state)
            # Removemos o melhor estado do heap e geramos seus estados
            generated = state.generate()
            for st in generated:
                # Para cada estado gerado adicionamos este no heap
                if st < state:
                    # best_state = st
                    heapq.heappush(self.heap, st)
            iterations -= 1
        return best_state
