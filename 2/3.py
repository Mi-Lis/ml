s1 = input()
s2 = [s1[i] for i in range(len(s1)) if i%2]
s = ""
for i in range(len(s2)-1, -1, -1):
    s+=s2[i]
print(s)