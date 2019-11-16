def swap_bit(bit_string, index):
    """
    Auxiliary function to swap individual bits of the string
    :param bit_string: string of bits
    :param index: index to swap bit
    :return: string of bits with swapped bit
    """
    if bit_string[index] == '0':
        new_bit_string = bit_string[:index] + '1' + bit_string[index + 1:]
    else:
        new_bit_string = bit_string[:index] + '0' + bit_string[index + 1:]
    return new_bit_string


class State:
    """
    Class representing the state of the allocating problem
    """

    def __init__(self, n_nurses=10, n_periods=21, scheduling='', restriction_weights=None):
        """
        :param n_nurses: number of nurses to be allocated
        :param n_periods: number of preriods to be filled by nurses
        :param scheduling: the current state of the scheduling
        :attr restriction_weights: the weight for each restriction
        """
        if restriction_weights is None:
            restriction_weights = [1, 1, 1, 1]
        self.n_nurses = n_nurses
        self.n_periods = n_periods
        self.scheduling = scheduling
        self.restriction_weights = restriction_weights

    def generate(self):
        """
        Method to generate the successor states
        :return: the successor states of the current state
        """
        generated = []

        for i in range(len(self.scheduling)):
            generated.append(State(self.n_nurses, self.n_periods, swap_bit(self.scheduling, i)))

        return generated

    def test(self):
        """
        Method to calculate the value of the heuristic
        :return: the sum of the restriction values
        """
        return (self.r1() * self.restriction_weights[0]
                + self.r2() * self.restriction_weights[1]
                + self.r3() * self.restriction_weights[2]
                + self.r4() * self.restriction_weights[3])

    def r1(self):
        """
        There must be at least 1 nurse and at most 3 nurses at each period
        :return: penalty for violating the restriction
        """
        turns = []
        for i in range(self.n_periods):
            turn = self.scheduling[i::self.n_periods]
            # Calcula se a quantidade de enfermeiros no turno satisfaz a restrição
            turns.append(not (1 <= sum([int(i) for i in turn]) <= 3))
        return sum(turns)

    def r2(self):
        """
        Each nurse must be allocated in 5 periods per week
        :return: penalty for violating the restriction
        """
        nurses = []
        for i in range(self.n_nurses):
            nurse = self.scheduling[i * self.n_periods: (i + 1) * self.n_periods]
            # Calcula quantos periodos da semana o enfermeiro trabalha
            nurses.append(abs(sum([int(i) for i in nurse]) - 5))
        return sum(nurses)

    def r3(self):
        """
        Nurses can't work more then 3 periods consecutive periods
        :return: penalty for violating the restriction
        """
        nurses = []
        for i in range(self.n_nurses):
            nurse = self.scheduling[i * self.n_periods: (i + 1) * self.n_periods]
            # Verifica se o enfermeiro trabalha mais de 3 periodos seguidos
            nurses.append('1111' in nurse)
        return sum(nurses)

    def r4(self):
        """
        Nurses prefer consistency in their scheduling. They prefer working the same period every day.
        :return: penalty for violating the restriction
        """
        nurses = []
        for i in range(self.n_nurses):
            nurse = self.scheduling[i * self.n_periods: (i + 1) * self.n_periods]
            # Descobre para cada turno(manha, noite, madrugada) se o enfermeiro trabalha
            nurses.append([nurse[i::3] for i in range(3)])
        inconsistencies = 0
        for n in nurses:
            # Para cada turno(manha, noite, madrugada) verifica se o enfermeiro trabalha neste
            morning = '1' in n[0]
            evening = '1' in n[1]
            night = '1' in n[2]
            # Verifica se o enfermeiro trabalha em turnos diferentes
            if (morning + evening + night) > 1:
                inconsistencies += 1
        return inconsistencies

    def __lt__(self, state):
        return self.test() < state.test()

    def __str__(self):
        state = ''
        for i in range(self.n_nurses):
            state += 'e{:02g}: '.format(i+1) + '[' + self.scheduling[i * self.n_periods: (i + 1) * self.n_periods] + ']' + '\n'
        state += 'Custo: ' + str(self.test())
        return state
