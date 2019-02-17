"""
    Problem: https://open.kattis.com/problems/herman
"""

import sys
import math

# Read input
R = sys.stdin.readline()
R = int(R)

# Calculate 
euclidian = R**2 * math.pi
taxicab = R**2 * 2 # In taxicab geometry the PI is 2

# Print results
print(euclidian)
print(taxicab)