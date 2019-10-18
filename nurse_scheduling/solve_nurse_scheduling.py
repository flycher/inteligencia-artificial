import argparse
import numpy as np

from search.HillClimbing import HillClimbing
from search.HillClimbingAclive import HillClimbingAclive
from search.BestFirst import BestFirst


parser = argparse.ArgumentParser(description='This program solves the Nurse scheduling problem using informed search.')
parser.add_argument('--algo', type=str, help='Informed search algorithm to use(HC, HCA, BF)', default='HC')
parser.add_argument('--nn', type=int, help='Number of nurses', default=10)
parser.add_argument('--np', type=int, help='Number of periods', default=3)
parser.add_argument('--sc', type=int, help='Schedule to be used', default=0)
# parser.add_argument('--path', type=int, help='Level of verbose for path printing('
#                                              '2 [Print path of all nodes],'
#                                              '1 [Print path only of objective state],'
#                                              '0 [Print only objective state])', default=0)

args = parser.parse_args()

if args.algo == 'HC':
    search = HillClimbing(args.nn, args.np)
elif args.algo == 'HCA':
    search = HillClimbingAclive(args.nn, args.np)
elif args.algo == 'BF':
    search = BestFirst(args.nn, args.np)
else:
    search = None


def get_random_schedule():
    schedule = np.zeros(7 * args.np * args.nn, dtype=int)
    allocated = np.random.choice(7 * args.np * args.nn, 7 * args.np * args.nn)
    schedule[allocated] = 1
    schedule = schedule.astype(str)
    schedule = ''.join(schedule)
    return schedule

def get_optimal_schedule():
    schedule = np.zeros(7 * args.np * args.nn, dtype=int)
    allocated = np.random.choice(7 * args.np * args.nn, 5 * args.nn)
    schedule[allocated] = 1
    schedule = schedule.astype(str)
    schedule = ''.join(schedule)
    return schedule

def get_init_schedule():
    return '0' * (7 * args.np * args.nn)


if args.sc == 1:
    schedule = get_init_schedule()
elif args.sc == 2:
    schedule = get_optimal_schedule()
elif args.sc == 3:
    schedule = get_random_schedule()
else:
    schedule = input('Type the initial schedule: ')

try:
    search.search(schedule)
except AttributeError:
    print('Unknown algorithm. Please use HC, HCA or BF')

