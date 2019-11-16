import argparse
import numpy as np

from search.SimulatedAnnealing import SimulatedAnnealing
from search.GeneticAlgorithm import GeneticAlgorithm

parser = argparse.ArgumentParser(description='This program solves the Nurse scheduling problem using '
                                             'simulated annealing or genetic algorithm.')
parser.add_argument('--algo', type=str, help='Informed search algorithm to use(SA: SimulatedAnnealing,'
                                             '                                 GA: GeneticAlgorithn.)', default='SA')
parser.add_argument('--nn', type=int, help='Number of nurses', default=10)
parser.add_argument('--np', type=int, help='Number of periods', default=3)
parser.add_argument('--temp', type=float, help='Initial temperature for SA', default=350)
parser.add_argument('--alpha', type=float, help='Temperature decreasing parameter for SA', default=0.99)
parser.add_argument('--it', type=int, help='Number of iterations for SA', default=1000)
parser.add_argument('--sc', type=int, help='Schedule to be used on SA(0: Reads user input,'
                                           '                          1: Starts without any nurses'
                                           '                          2: Starts with optimal numer of nurses,'
                                           '                          3: Starts with any number of nurses)', default=1)
parser.add_argument('--pop', type=int, help='Population size on GA', default=40)
parser.add_argument('--gen', type=int, help='Number of generations on GA', default=120)
parser.add_argument('--mut', type=float, help='Probability of mutation on GA', default=0.05)
parser.add_argument('--elite', type=float, help='Elitism percentage on GA', default=0.25)

args = parser.parse_args()


def get_random_schedule(n_periods_occupied):
    schedule_ = np.zeros(7 * args.np * args.nn, dtype=int)
    print(7 * n_periods_occupied)
    allocated = np.random.choice(7 * args.np * args.nn, 7 * n_periods_occupied)
    schedule_[allocated] = 1
    schedule_ = schedule_.astype(str)
    schedule_ = ''.join(schedule_)
    return schedule_


def get_init_schedule():
    return '0' * (7 * args.np * args.nn)


def get_schedule():
    schedule = ''
    if args.sc == 1:
        schedule = get_init_schedule()
    elif args.sc == 2:
        # TODO numero otimo de de enfermeiros dinamico
        schedule = get_random_schedule(50)
    elif args.sc == 3:
        schedule = get_random_schedule(np.random.randint(args.np * args.nn))
    return schedule


if args.algo == 'SA':
    search = SimulatedAnnealing(args.temp, args.it, args.alpha, args.nn, args.np)
    if args.sc == 0:
        search.search(input('Type in the schedule > '))
    else:
        best_state = search.search(get_schedule())
        print('The best state found was:')
        print(best_state)
elif args.algo == 'GA':
    search = GeneticAlgorithm(args.pop, args.gen, args.mut, args.elite, args.nn, args.np)
    best_state = search.search()
    print(best_state)
else:
    print('Unknown algorithm. Please use SA or GA')
