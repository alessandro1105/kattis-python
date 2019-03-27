"""
    Problem: https://open.kattis.com/problems/mia
"""

from sys import stdin

for line in stdin:
    if line.strip() == "0 0 0 0":
        break
    s0,s1,r0,r1 = tuple(map(int, line.split()))

    p1 = 0
    p2 = 0

    if (s0 == 1 and s1 == 2) or (s0 == 2 and s1 == 1): # P1 has Mia
        if (r0 == 1 and r1 == 2) or (r0 == 2 and r1 == 1):
            print("Tie.")
        else:
            print("Player 1 wins.")
    elif s0 == s1: # P1 has double
        if (r0 == 1 and r1 == 2) or (r0 == 2 and r1 == 1) or (r0 == r1 and s0 < r0):
            print("Player 2 wins.")
        elif (r0 == r1 and s0 == r0):
            print("Tie.")
        else:
            print("Player 1 wins.")
    else: # P1 has a simple roll
        if (r0 == 1 and r1 == 2) or (r0 == 2 and r1 == 1) or (r0 == r1):
            print("Player 2 wins.")
        else:
            p1 = 0
            p2 = 0
            if s0 > s1:
                p0 = s0*10 + s1
            else:
                p0 = s1*10 + s0

            if r0 > r1:
                p1 = r0*10 + r1
            else:
                p1 = r1*10 + r0

            if p0 > p1:
                print("Player 1 wins.")
            elif p0 < p1:
                print("Player 2 wins.")
            else:
                print("Tie.")

            

