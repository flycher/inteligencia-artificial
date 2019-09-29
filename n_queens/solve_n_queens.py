import argparse
from search.BFS import BFS
from search.DFS import DFS

parser = argparse.ArgumentParser(description='This program solves the N Queens problem using blind search.')
parser.add_argument('--algo', type=str, help='Blind search algorithm to use(BFS, DFS)', default='DFS')
parser.add_argument('--nq', type=int, help='Size of the board', default=8)
parser.add_argument('--path', type=int, help='Level of verbose for path printing('
                                             '2 [Print path of all nodes],'
                                             '1 [Print path only of objective state],'
                                             '0 [Print only objective state])', default=0)

args = parser.parse_args()

if args.algo == 'BFS':
    search = BFS(args.nq)
elif args.algo == 'DFS':
    search = DFS(args.nq)
else:
    search = None

try:
    search.solve(args.path)
except AttributeError:
    print('Unknown algorithm. Please use BFS or DFS')
