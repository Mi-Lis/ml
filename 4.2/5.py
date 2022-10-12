fo = open('input.txt', 'r')
fi = open('output.txt', 'w')
k = int(fo.readline())
s = [fo.readline() for _ in range(k)]
avg = []
for i in range(k):
    avg.append(sum([int(x) for x in s[i].split() if x in set(['1', '2', '3', '4', '5'])])/5)

s = sorted(list(zip(avg, s)))
avg, s = zip(*s)
fi.write(''.join(list(s)))