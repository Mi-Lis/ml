def no_scob(s):
    new_s = ""
    find_ls = False
    find_lr = False
    for x in s:
        if x == '(':
            find_ls = True
        if x == ')':
            find_lr = True
        if find_ls == False and find_lr == False:
            new_s+=x
        if find_ls == True and find_lr == False:
            new_s+=""
        if find_lr == True and find_ls == True:
            find_lr = False
            find_ls = False
    return new_s
n = int(input())
for _ in range(n):
    print(no_scob(input()))