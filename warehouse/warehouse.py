"""
    Problem: https://open.kattis.com/problems/warehouse
"""

T = int(input())

for _ in range(T):
    N = int(input())

    warehouse = {}
    for _ in range(N):
        toy, qty = input().split()

        if toy in warehouse:
            warehouse[toy] += int(qty)
        else:
            warehouse[toy] = int(qty)

    # Reorder
    warehouse = list(warehouse.items())
    warehouse.sort(key=lambda x: (-x[1], x[0]))

    print(len(warehouse))
    for toy in warehouse:
        print(" ".join(map(str, toy)))