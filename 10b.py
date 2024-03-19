f = open("input-03.txt", mode='r')

visited = set()

dir = 0
pos = [0, 0]

def visited_double():
    print("visited a position for a second time:", pos, abs(pos[0]) + abs(pos[1]))

for line in f.read().split(','):
    step = int(line.strip("RL \n"))

    if 'R' in line:
        dir = (dir + 1) % 4
    elif 'L' in line:
        dir = (dir - 1) % 4

    if dir == 0:
        for i in range(step):
            pos[0] += 1

            if (*pos, ) in visited:
                visited_double()
                exit()
            
            visited.add((*pos, ))

    elif dir == 1:
        for i in range(step):
            pos[1] += 1

            if (*pos, ) in visited:
                visited_double()
                exit()
            
            visited.add((*pos, ))

    elif dir == 2:
        for i in range(step):
            pos[0] -= 1

            if (*pos, ) in visited:
                visited_double()
                exit()
            
            visited.add((*pos, ))

    elif dir == 3:
        for i in range(step):
            pos[1] -= 1

            if (*pos, ) in visited:
                visited_double()
                exit()
            
            visited.add((*pos, ))

    

f.close()

print("pos (double visit not found):", pos, abs(pos[0]) + abs(pos[1]))