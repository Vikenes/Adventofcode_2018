# part 1 
f = open('data_1.txt')
data = [int(line) for line in f]

words = 0
for line in data:
    words += line
print(words)


# part 2
import sys

total = 0
f = open('data_1.txt', 'r')
data = [int(line) for line in f]
found = set()

while True:
    for line in data:
        total += line
        if total in found:
                sys.exit(print('The sequence first reaches %g twice' %total))
        found.add(total)
