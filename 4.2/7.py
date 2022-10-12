fo = open('input.txt', 'r')
fi = open('output.txt', 'w')
k = int(fo.readline())
s = [fo.readline() for _ in range(k)]
avg = []
for i in range(k):
    avg.append([int(x) for x in s[i].split()])

avg = [list(i) for i in zip(*avg)]
for i in range(k):
    avg[i] = sorted(avg[i])
avg = [list(i) for i in zip(*avg)]

for i in range(k):
    fi.write(' '.join([str(x) for x in avg[i]])+'\n')