import os
import pickle
from random import randint
from collections import deque

N = randint(0, 100)
history = deque([], 5)

if os.path.exists('history'):
    history = pickle.load(open('history', 'rb'))
else:
    history = deque([], 5)


def guess(k):
    if k == N:
        print('right')
        return True
    if k < N:
        print('less')
    else:
        print('high')
    return False


while True:
    line = input('input number')
    if line.isdigit():
        k = int(line)
        if guess(k):
            history.clear()
            break
        else:
            history.append(k)
    elif line == 'history':
        print(history)
    elif line == 'end':
        pickle.dump(history, open('history', 'wb'), True)
        os._exit(0)
