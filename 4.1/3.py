n, m= map(int, input().split())

def sort_min_last(a):
    i_min = a.index(min(a))
    temp = a[i_min]
    a[i_min] = a[len(a)-1]
    a[len(a)-1] = temp
    return a


a = [map(int, input().split()) for _ in range(n) ]

a = [list(i) for i in zip(*a)]
for i in range(m):
    a[i] = sort_min_last(a[i])

a = [list(i) for i in zip(*a)]

for i in range(n):
    print(' '.join(map(str, a[i])))
