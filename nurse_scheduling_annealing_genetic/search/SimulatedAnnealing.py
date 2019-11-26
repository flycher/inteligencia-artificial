import numpy as np
from search.SchedulingProblemSearch import SchedulingProblemSearch
from search.State import State


class SimulatedAnnealing(SchedulingProblemSearch):
    """
    A class for executing Simulated Annealing for the scheduling problem
    """

    def __init__(self, initial_temperature=350, max_iterations=1000, alpha=0.99,
                 n_nurses=10, n_periods=3, restriction_weights=None):
        super().__init__(n_nurses, n_periods, restriction_weights)
        self.temperature = initial_temperature
        self.max_iterations = max_iterations
        self.alpha = alpha

    def search(self, schedule):
        state = State(self.n_nurses, self.n_periods, schedule)
        while self.temperature > 0 and self.max_iterations > 0:
            # gera um novo estado aleatório apartir no atual
            new_state = state.generate_random()
            # calcula a diferenca de energia entre os estados
            delta_e = new_state.test() - state.test()
            probability = self.probability(delta_e)
            r = np.random.rand()
            # define se o estado será mudado
            chosen = probability > r
            print('Temperature:', self.temperature, 'Probability:', probability, 'Chosen:', chosen)
            print(new_state)
            if chosen:
                state = new_state
            # atualiza a temperatura
            self.update_temperature()
            self.max_iterations -= 1
        return state

    def probability(self, delta_e):
        """
        Calculates the probability to move between states
        :param delta_e: difference in  energy from states
        :return: probability to move states
        """
        if delta_e < 0:
            return 1
        return np.exp((-delta_e) / self.temperature)

    def update_temperature(self):
        """
        Updates the temperature according to alpha
        :return: new temperature
        """
        self.temperature *= self.alpha
