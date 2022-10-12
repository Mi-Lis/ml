
def is_pow5(x):
    while x% 5 ==0:
        x = x//5
    if x ==1:
        return True
    else: 
        return False    

n = int(input())
s = map(int, input().split())
c = 0

for x in s:
    if is_pow5(x):
        c+=1

print(c)
