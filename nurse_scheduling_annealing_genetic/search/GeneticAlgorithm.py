import numpy as np
from search.SchedulingProblemSearch import SchedulingProblemSearch
from search.State import State


class GeneticAlgorithm(SchedulingProblemSearch):
    """
    A class for executing a Genetic Algorithm for the scheduling problem
    """

    def __init__(self, population_size=40, generations=120, mutation=0.05, elitism=0.25,
                 n_nurses=10, n_periods=3, restriction_weights=None):
        super().__init__(n_nurses, n_periods, restriction_weights)
        self.population_size = population_size
        self.generations = generations
        self.mutation = mutation
        self.elitism = int(population_size * elitism)

    def search(self):
        population = self.generate_population()

        population.sort()
        best_chromosome = population[0]
        print('Generation 000')
        [print('index:', i, 'chromosome', hex(int(p.scheduling, 2)), 'fitness:', p.test()) for i, p in enumerate(population)]

        for i in range(1, self.generations + 1):
            # seleciona os cromossomos mais aptos
            elite = population[:self.elitism]
            # cria uma nova geração
            new_generation, crossovers = self.crossover_and_mutate(population, self.population_size - self.elitism)
            # cria uma nova população com a nova geração e a elite
            population = elite + new_generation
            crossovers = ([(-1, -1)] * self.elitism) + crossovers
            print('Generation {:03d}'.format(i))
            [print('index:', i,
                   'chromosome', hex(int(p.scheduling, 2)),
                   'parents:', c,
                   'fitness:', p.test()) for
             i, (p, c) in enumerate(zip(population, crossovers))]
            population.sort()
            if population[0] < best_chromosome:
                best_chromosome = population[0]

        return best_chromosome

    def generate_population(self):
        """
        Generates the initial population of random chromosomes
        :return: list of random states
        """
        population = []
        for i in range(self.population_size):
            population.append(State(self.n_nurses, self.n_periods, self.get_random_schedule()))

        return population

    def get_random_schedule(self):
        """
        Generates a random schedule
        This schedule can have any number of nurses
        :return: random schedule
        """
        len_schedule = self.n_nurses * self.n_periods
        schedule = np.zeros(len_schedule, dtype=int)
        allocated = np.random.choice(len_schedule, np.random.randint(len_schedule))
        schedule[allocated] = 1
        schedule = schedule.astype(str)
        schedule = ''.join(schedule)
        return schedule

    def crossover_and_mutate(self, population, generation_size):
        """
        Executes crossover and mutation in a population of chromosomes
        :param population: current population
        :param generation_size: size of the new generation of chromosomes
        :return: new generation of chromosomes
        """
        # transforma uma lista de strings em um numpy array de strings
        pop = np.array(population)
        # seleciona generation_size * 2 elementos da população com repetição
        selected = np.random.choice(pop, generation_size * 2)
        new_generation = []
        crossovers = []
        len_schedule = self.n_nurses * self.n_periods

        for i in range(generation_size):
            # seleciona dois cromossomos aleatórios da população
            c1 = selected[i]
            c2 = selected[-(i + 1)]
            # seleciona um ponto de cruzamento aleatório
            cross_point = np.random.randint(len_schedule)
            # realiza o cruzamento dos cromossomos
            new_c = c1.scheduling[:cross_point] + c2.scheduling[cross_point:]
            new_c = State(self.n_nurses, self.n_periods, new_c)
            # possibilidade de mutação de um cromossomo
            if np.random.rand() <= self.mutation:
                new_c.mutate(cross_point)
            # adiciona o cromossomo e seus pais
            new_generation.append(new_c)
            crossovers.append((np.argwhere(pop == c1)[0][0], np.argwhere(pop == c2)[0][0]))

        return new_generation, crossovers

