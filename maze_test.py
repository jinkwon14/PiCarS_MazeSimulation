import numpy as np


maze = [['c', 'u', 'c', 'u', 'c', 'u', 'c'],    #0
          ['u', 'n', 'u', 'n', 'u', 'n', 'u'],    #1
          ['c', 'u', 'c', 'u', 'c', 'u', 'c'],    #2
          ['u', 'n', 'u', 'n', 'u', 'n', 'u'],    #3
          ['c', 'u', 'c', 'u', 'c', 'u', 'c'],    #4
          ['u', 'n', 'u', 'n', 'u', 'n', 'u'],    #5
          ['c', 'u', 'c', 'u', 'c', 'u', 'c']]    #6

maze = np.matrix(maze)

# Possible starting positions: (6, 1), (6, 3), (6, 5)

def print_maze():
    for el in maze:
        print(el)
# There is a wall in the front if

print_maze()
