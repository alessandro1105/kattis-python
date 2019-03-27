"""
    Problem: https://open.kattis.com/problems/4thought
"""

def calculate(n):
    for c1 in couple:
        for o in operands:
            for c2 in couple:
                result = eval(c1 + o + c2)
                if round(result) == n:
                    return [c1, o, c2]

    return []

m = int(input())

operands = ["+", "-", "*", "/"]
couple = ["4 + 4", "4 - 4", "4 * 4", "4 / 4"]

for _ in range(m):
    n = int(input())

    expression = calculate(n)

    if len(expression) == 3:
        print(" ".join(expression) + " = " + str(n))
    else:
        print("no solution")
    
   
                    


    