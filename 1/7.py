from math import ceil, log


s = input().split()
a = int(s[0])
b = int(s[1])

d1 = 0
d2 = 0
while b//3>a:
    b = b//3
    d1+=1
d2 = max(ceil(log(b/a, 3)), 0)+1
print(d1, d2)