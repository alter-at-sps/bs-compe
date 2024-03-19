f = open("input.txt", mode='r')

matching_count = 0

for line in f:
    # parse

    intervals = line.split(',')
    
    i1 = intervals[0].split('-')
    i1 = (int(i1[0]), int(i1[1]))

    i2 = intervals[1].split('-')
    i2 = (int(i2[0]), int(i2[1]))

    if (i1[0] >= i2[0] and i1[0] <= i2[1]) or (i2[0] >= i1[0] and i2[0] <= i1[1]):
        matching_count += 1
        print(line.strip())

f.close()

print("matching count:", matching_count)