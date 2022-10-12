def no_even(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] % 2 == 0:
                a[i][j] = 0
    return a
n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

if no_even(a) == no_even(b):
    print("YES")
else:
    print("NO")

