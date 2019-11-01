import argparse
import numpy as np

from search.HillClimbing import HillClimbing
from search.HillClimbingSteepestAscent import HillClimbingSteepestAscent
from search.BestFirst import BestFirst
from search.State import State

parser = argparse.ArgumentParser(description='This program solves the Nurse scheduling problem using informed search.')
parser.add_argument('--algo', type=str, help='Informed search algorithm to use(HC: Hill Climbing,'
                                             '                                 HCA: Hill Climbing Steepest Aclive,'
                                             '                                 BF: Best First)', default='HC')
parser.add_argument('--nn', type=int, help='Number of nurses', default=10)
parser.add_argument('--np', type=int, help='Number of periods', default=3)
parser.add_argument('--sc', type=int, help='Schedule to be used(0: Reads user input,'
                                           '                    1: Starts without any nurses'
                                           '                    2: Starts with optimal numer of nurses,'
                                           '                    3: Starts with any number of nurses)', default=1)
parser.add_argument('--it', type=int, help='Number of iterations of the search', default=1)
parser.add_argument('--file', type=str, help='File with schedules.', default=None)

args = parser.parse_args()

if args.algo == 'HC':
    search = HillClimbing(args.nn, args.np)
elif args.algo == 'HCA':
    search = HillClimbingSteepestAscent(args.nn, args.np)
elif args.algo == 'BF':
    search = BestFirst(args.nn, args.np)
else:
    search = None


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


try:
    best_state = State(args.nn, args.np, get_init_schedule())
    if args.sc == 0:
        search.search(input('Type in the schedule > '))
    elif args.file is not None:
        i = 1
        with open(args.file, 'r') as f:
            print('#' * 20, 'Iteration {}'.format(i), '#' * 20)
            schedule = f.readline()
            schedule = schedule.strip()
            best_state = search.search(schedule)
            i += 1
            schedule = f.readline()
            while schedule:
                schedule = schedule.strip()
                print('#' * 20, 'Iteration {}'.format(i), '#' * 20)
                state = search.search(schedule)
                if state < best_state:
                    best_state = state
                schedule = f.readline()
                i += 1
        print()
        print('The best state found was:')
        print(best_state)
    else:
        print('#' * 20, 'Iteration {}'.format(1), '#' * 20)
        best_state = search.search(get_schedule())
        for i in range(2, args.it + 1):
            print('#' * 20, 'Iteration {}'.format(i), '#' * 20)
            state = search.search(get_schedule())
            if state < best_state:
                best_state = state
        print()
        print('The best state found was:')
        print(best_state)
except AttributeError:
    print('Unknown algorithm. Please use HC, HCA or BF')
