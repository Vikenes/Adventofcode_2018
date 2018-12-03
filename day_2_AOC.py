from collections import Counter

f = open('data_2.txt', 'r')
data = [list(line[:-1]) for line in f]

two = 0
three = 0
for value in data:
    count = Counter(value)
    for letter in count:
        if 2 in count.values():
            two += 1
        if 3 in count.values():
            three += 1
        break

print(two*three)

# part 2 
import sys

f = open('data_2.txt', 'r')
data = [(line[:-1]) for line in f]

for i in range(len(data)):
    for k in range(len(data)):
        nod = 0 # number of differences
        for j in range(len(data[0])):
            if data[i][j] != data[k][j]:
                nod += 1

        if nod == 1:
            a = data[k]
            c = data[i]
            for m in range(len(data[i])):
                if a[m] != c[m]:
                    d = c[:m] + c[m+1:]
            sys.exit(d)
