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
        state = State(self.n_nurses, self.n_periods, scheduling)
        heapq.heappush(self.heap, state)
        while True:
            print(state)
            # Removemos o melhor estado do heap e geramos seus estados
            state = heapq.heappop(self.heap)
            generated = state.generate()
            for st in generated:
                # Para cada estado gerado adicionamos este no heap
                if st.test() < state.test():
                    heapq.heappush(self.heap, st)
            # Verificamos se este estado gerado melhor tem custo menor que seu gerador
            improved = (self.heap != []) and self.heap[0].test() < state.test()
            # improved = self.heap[0].test() < state.test()
            if not improved:
                break
        return state
