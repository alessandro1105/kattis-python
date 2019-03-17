"""
    Problem: https://open.kattis.com/problems/alphabetspam
"""

import sys

# Read the line
line = sys.stdin.readline()
line = line.rstrip()

whitespaces = 0
lowercases = 0
uppercases = 0
symbols = 0

for char in line:
    if char == '_':
        whitespaces += 1

    elif char.isalpha():
        if char.isupper():
            uppercases += 1
        else:
            lowercases += 1

    else:
        symbols += 1


print(whitespaces / len(line))
print(lowercases / len(line))
print(uppercases / len(line))
print(symbols / len(line))