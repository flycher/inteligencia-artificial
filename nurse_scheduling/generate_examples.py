import numpy as np

with open('testes.txt', 'w') as f:
    for i in range(10):
        zeros = np.zeros(210, dtype=int)
        ones = np.random.choice(210, np.random.randint(210))
        zeros[ones] = 1
        print(''.join([str(n) for n in zeros]), file=f)
