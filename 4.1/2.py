from math import ceil


def is_prime(a):
    if a in [2, 3]:
        return True
    for i in range(2,round(a/2)+1):
        if a%i == 0:
            return False
    return True
N = int(input())

for i in range(2, N):
    if is_prime(i) and is_prime(N-i):
        print(i,N-i)
        break