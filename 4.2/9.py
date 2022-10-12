fo = open('input.txt', 'r')
fi = open('output.txt', 'w')
k = int(fo.readline())
s = [fo.readline() for _ in range(k)]
stop = fo.readline()

avg = []
for i in range(k):
    avg.append([x for x in s[i].split()])

new_avg = []
for i in range(k):
    if avg[i][1] == stop:
        continue
    new_avg.append(avg[i])

n = []
for i in range(len(new_avg)):
    n.append(new_avg[i][0])
print(n)
print(new_avg)
new_avg = sorted(list(zip(n, new_avg)))

n, new_avg = zip(*new_avg)


for i in range(len(new_avg)):
    fi.write(' '.join([str(x) for x in new_avg[i]])+'\n')