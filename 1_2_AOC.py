import sys

def readfile2(filename):
    total = 0
    noi = 0 # number of iterations
    infile = open(filename, 'r')
    iteration = []
    while True:
        for line in infile:
            noi += 1
            print(noi)

            if line.find('+') != -1:
                total += int(line[1:-1])
                if total in iteration:
                    print('The sequence first reaches %g twice' %total)
                    sys.exit()

                iteration.append(total)

            elif line.find('-') != -1:
                total -= int(line[1:-1])
                if total in iteration:
                    print('The sequence first reaches %g twice' %total)
                    sys.exit()
                iteration.append(total)

readfile2('data_1_1.txt')
