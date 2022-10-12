def matmult(a,b):
    zip_b = zip(*b)
    zip_b = list(zip_b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b))
             for col_b in zip_b] for row_a in a]

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


n = int(input())
s = [list(map(float, input().split())) for _ in range(n)]

for i in range(n-1):
    s = matmult(s, s)

arr = []
for i in range(n):
    arr.append([])
    for j in range(n):
        arr[i].append(toFixed(s[i][j],3))

for i in range(n):
    print(' '.join( arr[i]))
