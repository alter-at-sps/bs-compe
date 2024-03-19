triples = []

# pre sum triples

f = open("input.txt", mode='r')

i = 0

while True:
    line = f.readline()

    if line == "":
        break
    
    value = int(line)

    # append new triple
    triples.append(0)

    for j in range(3):
        if i - j < 0:
            break

        triples[i - j] += value

    i += 1

f.close()

# same as 01a

count = 0
last_line = None

while True:
    if len(triples) == 0:
        print("total matches: ", count)
        exit()

    line = triples.pop(0)

    if not last_line == None:
        if int(last_line) < int(line):
            count += 1

    last_line = line