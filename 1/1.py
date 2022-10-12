import functools
n = list(input())
n = [int(digit) for digit in n]
s = sum(map(int,n))
print(s)
s = functools.reduce(lambda x, y: x*y, n)
print(s)