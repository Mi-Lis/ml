import collections
s = input()
s_d = collections.Counter(s)
s_s = set(s)
ans = ""
for key, value in s_d.items():
    if s_d[key] == 1:
        ans+=key
print(''.join(sorted(ans)))
