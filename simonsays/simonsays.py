"""
    Problem: https://open.kattis.com/problems/simonsays
"""

import sys

# Read how many command
n = sys.stdin.readline()
n = int(n)

for i in range(n):
    command = sys.stdin.readline()

    if (command.find('Simon says ') == 0):
        print(command[11:])
