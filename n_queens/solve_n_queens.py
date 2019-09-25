import argparse
from search.BFS import BFS
from search.DFS import DFS

parser = argparse.ArgumentParser(description='This program solves the N Queens problem using blind search.')
parser.add_argument('--algo', type=str, help='Blind search algorithm to use(BFS, DFS)', default='DFS')
parser.add_argument('--nq', type=int, help='Size of the board', default=8)
args = parser.parse_args()

if args.algo == 'BFS':
    search = BFS(args.nq)
elif args.algo == 'DFS':
    search = DFS(args.nq)
else:
    search = None

try:
    search.solve()
except AttributeError:
    print('Unknown algorithm. Please use BFS or DFS')
