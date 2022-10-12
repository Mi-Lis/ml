n = int(input())
i = 0
i_max = 0
max = -100001

for i in range(n):
    i+=1
    x = abs(int(input()))
    if x >= max:
        i_max = i
        max = x

print(i_max)
