n = int(input())
m = [int(input()) for _ in range(n)]
k = int(input())
m = [str(k*x) for x in m]
m = ' '.join(m)
print(m)