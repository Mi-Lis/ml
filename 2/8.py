from math import pi, sqrt
def square_perimetr_p(a, b):
    return a*b, 2*(a+b)

def square_perimetr_t(a, b, c):
    return sqrt((a+b+c)/2*((a+b+c)/2-a)*((a+b+c)/2-b)*((a+b+c)/2-c)), a+b+c

def square_perimetr_k(r):
    return pi*r**2, 2*pi*r


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

s = input().split()
pl, pr = 0, 0
if s[0] == 'k':
    pl, pr = square_perimetr_k(float(s[1]))
if s[0] == 't':
    pl, pr = square_perimetr_t(float(s[1]), float(s[2]), float(s[3]))
if s[0] == 'p':
    pl, pr = square_perimetr_p(float(s[1]), float(s[2]))

print(toFixed(pr, 4), toFixed(pl, 4))


