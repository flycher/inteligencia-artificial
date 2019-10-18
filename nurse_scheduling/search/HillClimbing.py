from search.SchedulingProblemSearch import SchedulingProblemSearch
from search.State import State


class HillClimbing(SchedulingProblemSearch):
    """
    A class for the execution of the Hill Climbing seach for the scheduling problem
    """
    def __init__(self, n_nurses=10, n_periods=3):
        super().__init__(n_nurses, n_periods)

    def search(self, scheduling):
        """
        The actual schedule
        :param scheduling: The actual schedule to be optimized
        :return: The new scheduled with reduced violation cost
        """
        state = State(self.n_nurses, self.n_periods, scheduling)

        while True:
            print(state)
            generated = state.generate()
            improved = False
            for st in generated:
                # Se atual possui um custo menor que seu gerador, exploramos este estado
                if st.test() < state.test():
                    state = st
                    improved = True
                    break
            if not improved:
                break
        return state
