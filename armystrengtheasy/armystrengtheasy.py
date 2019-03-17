"""
    Problem: https://open.kattis.com/problems/armystrengtheasy
"""

T = int(input())

for _ in range(T):
    # Discard first and second line
    input()
    input()
    god = [int(x) for x in input().split()]
    mega = [int(x) for x in input().split()]

    # Battle!
    while len(god) > 0 and len(mega) > 0:
        god.sort()
        mega.sort()

        # Get the weakest soldier
        weakest = min(god[0], mega[0])

        if weakest in mega:
            mega.remove(weakest)
        else:
            god.remove(weakest)

    if len(god) > 0:
        print("Godzilla")
    else:
        print("MechaGodzilla")