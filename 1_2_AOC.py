import sys

def readfile2(filename):
    total = 0
    noi = 0 # number of iterations
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
