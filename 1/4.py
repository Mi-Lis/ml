n = int(input())

suffix = "лет"
if (n//10)%10 != 1:
        if n%10 == 1:
            suffix = "год"
        elif n%10 in (2,3,4):
            suffix = "года"
print("Мне", n, suffix)