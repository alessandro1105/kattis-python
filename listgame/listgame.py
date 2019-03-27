"""
    Problem: https://open.kattis.com/problems/listgame
"""

def is_prime(n):
    i = 2

    while i*i <= n:
        if n % i == 0:
            return False
        i += 1

    return True

def factors(n):
    while (n > 1):
        if (is_prime(n)):
            n = 1
            yield n
            break
        for div in range(2, n +1):
            if n % div == 0:
                n //= div
                yield div
                break

n = int(input())

if is_prime(n):
    print(1)
else:
    print(sum(1 for x in factors(n)))