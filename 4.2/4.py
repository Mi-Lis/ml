fo = open('input.txt', 'r')
fi = open('output.txt', 'w')
s = fo.readlines()
k = s.index(max(s))+1

fi.write(str(k))