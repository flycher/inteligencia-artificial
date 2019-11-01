from search.SchedulingProblemSearch import SchedulingProblemSearch
from search.State import State


class HillClimbingSteepestAscent(SchedulingProblemSearch):
    """
    A class for executing the Hill Climbing with Steepest-Ascent for the scheduling problem
    """
    def __init__(self, n_nurses=10, n_periods=3, restriction_weights=None):
        if restriction_weights is None:
            restriction_weights = [1, 1, 1, 1]
        super().__init__(n_nurses, n_periods, restriction_weights)

    def search(self, scheduling):
        state = State(self.n_nurses, self.n_periods, scheduling)
        while True:
            print(state)
            generated = state.generate()
            # Exploraremos o estado geraco com menor custo
            best = generated[0]
            improved = False
            for st in generated[1:]:
                # Se atual possui um custo menor que o melhor atual
                if st.test() < best.test():
                    best = st
            improved = best.test() < state.test()
            # Verificamos se este estado gerado melhor tem custo menor que seu gerador
            if not improved:
                break
            state = best
        return state
