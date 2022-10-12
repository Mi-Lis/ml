
s1 = input()
s2 = input()


s1_s = set(s1)
s2_s = set(s2)

ans = "True"

if s2_s.issubset(s1_s):
    for x in s2:
        flag = (s1.count(x)>=s2.count(x))
        if not flag:
            ans = "False"
            break
    print(ans)
else:
    print("False")