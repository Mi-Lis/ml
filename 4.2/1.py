fo = open('input.txt', 'r')
fi = open('output.txt', 'w')
s = ""
k = int(fo.readline())
for i in fo.readlines():
    if  len(i)>=k and i[k-1]!='\n':
        s+=i[k-1]

fi.write(s)