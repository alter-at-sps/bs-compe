f = open("input.txt", mode='r')

pos = [0, 0]

for line in f:
    if "forward" in line:
        pos[0] += int(line.strip("forward \n"))
    elif "up" in line:
        pos[1] -= int(line.strip("up \n"))
    elif "down" in line:
        pos[1] += int(line.strip("down \n"))
    else:
        print("invalid instruction:", line)

f.close()

print("final sub pos:", pos, pos[0] * pos[1])