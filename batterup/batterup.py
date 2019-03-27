"""
    Problem: https://open.kattis.com/problems/batterup
"""

n = int(input())

bats = [int(x) for x in input().split() if x != "-1"]

print(sum(bats) / len(bats))