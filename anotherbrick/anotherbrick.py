"""
    Problem: https://open.kattis.com/problems/anotherbrick
"""

import sys

arguments = sys.stdin.readline()
arguments = arguments.split()

h = int(arguments[0])
w = int(arguments[1])
n = int(arguments[2])

arguments = sys.stdin.readline()
arguments = arguments.split()
bricks = []
for i in range(n):
    bricks.append(int(arguments[i]))

# Check if the wall can be built
height = 0
width = 0
for i in range(n):
    if (width + bricks[i] < w):
        width += bricks[i]
    
    elif (width + bricks[i] == w):
        width = 0
        height += 1
    
    else:
        break
    
    if (height == h and width == 0):
        break

if (height == h and width == 0):
    print('YES')
else:
    print('NO')