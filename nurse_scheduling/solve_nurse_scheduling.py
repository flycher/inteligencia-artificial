import argparse
import numpy as np

from search.HillClimbing import HillClimbing
from search.HillClimbingSteepestAscent import HillClimbingSteepestAscent
from search.BestFirst import BestFirst

parser = argparse.ArgumentParser(description='This program solves the Nurse scheduling problem using informed search.')
parser.add_argument('--algo', type=str, help='Informed search algorithm to use(HC, HCA, BF)', default='HC')
parser.add_argument('--nn', type=int, help='Number of nurses', default=10)
parser.add_argument('--np', type=int, help='Number of periods', default=3)
parser.add_argument('--sc', type=int, help='Schedule to be used', default=1)

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
    allocated = np.random.choice(7 * args.np * args.nn, 7 * n_periods_occupied)
    schedule_[allocated] = 1
    schedule_ = schedule_.astype(str)
    schedule_ = ''.join(schedule_)
    return schedule_


def get_init_schedule():
    return '0' * (7 * args.np * args.nn)


if args.sc == 1:
    schedule = get_init_schedule()
elif args.sc == 2:
    schedule = get_random_schedule(5 * args.np)
elif args.sc == 3:
    schedule = get_random_schedule(7 * args.np * args.nn)
else:
    schedule = input('Type the initial schedule: ')


try:
    search.search(schedule)
except AttributeError:
    print('Unknown algorithm. Please use HC, HCA or BF')
