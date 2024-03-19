f = open("input.txt", mode='r')

count = 0
last_line = None

while True:
    line = f.readline()

    if line == "":
        print("total matches: ", count)
        
        f.close()
        exit()

    if not last_line == None:
        if int(last_line) < int(line):
            count += 1

    last_line = line