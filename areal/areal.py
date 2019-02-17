"""
    Problem: https://open.kattis.com/problems/areal
"""

import sys
import math

# Read area
area = sys.stdin.readline()
area = int(area)

# Calculate the fence length
fence = 4 * math.sqrt(area)

# Print the result
print(fence)