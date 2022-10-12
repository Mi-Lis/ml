import numpy as np
n, m = map(int, input().split())

a = np.array( [list(map(int, input().split())) for _ in range(n)])
a = a.transpose()

arr = []

for i in range(m):
    arr.append([])
    for j in range(n):
        arr[i].append(str(a[i][j]))

for i in range(m):
    print(' '.join( arr[i]))