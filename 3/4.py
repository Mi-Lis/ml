n = input()
s = input().split()

ans = [x for x in s if len(set(x)) != len(x)]
ans = ' '.join(ans)
print(ans)
