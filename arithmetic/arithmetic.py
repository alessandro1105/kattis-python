"""
    Problem: https://open.kattis.com/problems/arithmetic
"""

import sys

# Read the number as a string
n = sys.stdin.readline()

# Convert the string into a number
n8 = int(n, 8)

print((hex(n8)[2:]).upper())