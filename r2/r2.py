"""
    Problem: https://open.kattis.com/problems/r2
"""

import sys

# Read input
numbers = sys.stdin.readline()
numbers = numbers.split()
R1 = int(numbers[0])
S = int(numbers[1])

# Calculate 
R2 = S * 2 - R1

# Print R2
print(R2)