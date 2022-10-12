fo = open('input.txt', 'r')
fi = open('output.txt', 'w')
k = int(fo.readline())
s = [fo.readline() for _ in range(k)]
avg = []
for i in range(k):
    avg.append(sum([int(x) for x in s[i].split() if '1950'<=x<='2000' ]))

s = sorted(list(zip(avg, s)), reverse=True)
avg, s = zip(*s)
s = list(s)
s[0]+='\n'
fi.write(''.join(list(s)))