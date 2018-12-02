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
