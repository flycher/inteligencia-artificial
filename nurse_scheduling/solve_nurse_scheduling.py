import argparse
import numpy as np

from search.HillClimbing import HillClimbing
from search.HillClimbingAclive import HillClimbingAclive
from search.BestFirst import BestFirst


parser = argparse.ArgumentParser(description='This program solves the Nurse scheduling problem using informed search.')
parser.add_argument('--algo', type=str, help='Informed search algorithm to use(HC, HCA, BF)', default='HC')
parser.add_argument('--nn', type=int, help='Number of nurses', default=10)
parser.add_argument('--np', type=int, help='Number of periods', default=3)
parser.add_argument('--sc', type=bool, help='Schedule to use', default=True)
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


def get_schedule(n_nurses):
    if args.sc:
        schedule = np.zeros(21 * n_nurses, dtype=int)
        allocated = np.random.choice(21 * n_nurses, 5 * n_nurses)
        schedule[allocated] = 1
        schedule = schedule.astype(str)
        schedule = ''.join(schedule)
    else:
        schedule = '0' * 210
    return schedule


try:
    search.search(get_schedule(args.nn))
except AttributeError:
    print('Unknown algorithm. Please use HC, HCA or BF')

