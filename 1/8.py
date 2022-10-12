def is_prime(x):
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return print("No")
    return print("Yes")

is_prime(int(input()))