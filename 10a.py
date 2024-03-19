f = open("input-03.txt", mode='r')

dir = 0
pos = [0, 0]

for line in f.read().split(','):
    step = int(line.strip("RL \n"))

    if 'R' in line:
        dir = (dir + 1) % 4
    elif 'L' in line:
        dir = (dir - 1) % 4

    if dir == 0:
        pos[0] += step
    elif dir == 1:
        pos[1] += step
    elif dir == 2:
        pos[0] -= step
    elif dir == 3:
        pos[1] -= step

f.close()

print("pos:", pos, abs(pos[0]) + abs(pos[1]))