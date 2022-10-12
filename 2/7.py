n,m,k = map(int, input().split())
a = input().split()
a = [int(x) for x in a]

s = sum([x for x in a if abs(x)%10 == k and abs(x)%m!=0])
print(s)