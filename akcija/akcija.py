"""
    Problem: https://open.kattis.com/problems/akcija
"""

N = int(input())
prices = [int(input()) for _ in range(N)]

prices.sort()
price = 0

group = []
for x in range(len(prices)):
    group.append(prices.pop())

    if (len(group) == 3):
        price += sum(group) - min(group)
        group = []
        

price += sum(group)
print(price)