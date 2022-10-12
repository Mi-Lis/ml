n = int(input())
s = input().split()
s = [int(x) for x in s]
s[s.index(max(s))] = -s[s.index(max(s))]
s = [str(x) for x in s]
s = ' '.join(s)
print(s)