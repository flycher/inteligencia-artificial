class SchedulingProblemSearch:

    def __init__(self, n_nurses=10, n_periods=3, restriction_weights=None):
        if restriction_weights is None:
            restriction_weights = [1, 1, 1, 1]
        self.n_nurses = n_nurses
        self.n_periods = n_periods * 7
        self.restriction_weights = restriction_weights
