f = open("input.txt", mode='r')

sink_vel = 0
pos = [0, 0]

for line in f:
    if "forward" in line:
        dist = int(line.strip("forward \n"))

        pos[0] += dist
        pos[1] += sink_vel * dist
    elif "up" in line:
        sink_vel -= int(line.strip("up \n"))
    elif "down" in line:
        sink_vel += int(line.strip("down \n"))
    else:
        print("invalid instruction:", line)

f.close()

print("final sub pos:", pos, pos[0] * pos[1])