def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"
n = float(input())
s = 1.0000
while n > 0:
    s*=n
    n = float(input())
    
print(toFixed(s, 6))