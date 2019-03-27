"""
    Problem: https://open.kattis.com/problems/aboveaverage
"""

C = int(input())

for _ in range(C):
    N, *grades = tuple(map(int, input().split()))

    mean = sum(grades) / N

    above = 0
    for grade in grades:
        if grade > mean:
            above += 1
    
    print("%.3f%s" % (round(above / N * 100, 3), '%'))