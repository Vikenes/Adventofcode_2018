# part 1 

def readfile1(filename):
    infile = open(filename, 'r')
    words = 0
    for line in infile:

        if line.find('+') != -1:
            words += float(line[1:-1])
        elif line.find('-') != -1:
            words -= float(line[1:-1])
        print(words)

readfile1('data_1_1.txt')


# part 2
import sys

def readfile2(filename):
    total = 0
    infile = open(filename, 'r')
    iteration = []
    while True:
        infile.seek(0,0)
        for line in infile:
            if line.find('+') != -1:
                total += int(line[1:-1])
                if int(total) in iteration:
                    sys.exit(print('The sequence first reaches %g twice' %total))
                iteration.append(int(total))

            elif line.find('-') != -1:
                total -= int(line[1:-1])
                if int(total) in iteration:
                    sys.exit(print('The sequence first reaches %g twice' %total))
                iteration.append(int(total))

readfile2('data_1_1.txt')
