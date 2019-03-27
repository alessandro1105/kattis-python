"""
    Problem: https://open.kattis.com/problems/different
"""

from sys import stdin

for line in stdin.readlines():
    a, b = tuple(map(int, line.split()))

    print(abs(a - b))