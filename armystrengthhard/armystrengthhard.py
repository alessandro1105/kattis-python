"""
    Problem: https://open.kattis.com/problems/armystrengthhard
"""

T = int(input())

for _ in range(T):
    # Discard first and second line
    input()
    input()
    
    max_g = 0 # Max number of Godzilla
    max_g_n = 0 # Numero or occurences
    max_m = 0 # Max number of Godzilla
    max_m_n = 0 # Numero or occurences
    
    # Godzilla
    for x in input().split():
        x = int(x)
        if x > max_g:
            max_g = x
            max_g_n = 0
        elif x == max_g:
            max_g_n += 1
    
    # MechaGodzilla
    for x in input().split():
        x = int(x)
        if x > max_m:
            max_m = x
            max_m_n = 0
        elif x == max_m:
            max_m_n += 1

    if (max_g > max_m) or (max_g == max_m and max_g >= max_m):
        print("Godzilla")
    elif max_g < max_m:
        print("MechaGodzilla")
    