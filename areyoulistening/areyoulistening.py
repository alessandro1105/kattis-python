"""
    Problem: https://open.kattis.com/problems/areyoulistening
"""

import math

cx, cy, n = tuple(map(int, input().split()))

distances = []
for i in range(n):
    x, y, r = tuple(map(int, input().split()))

    # Calculate the distance
    distance = math.sqrt((cx - x)**2 + (cy - y)**2) - r
    distances.append(distance)

# Sort distances
distances.sort()

# Get the 3rd
radius = math.floor(distances[2])

if (radius < 0):
    print(0)
else:
    print(radius)