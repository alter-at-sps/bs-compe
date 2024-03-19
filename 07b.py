f = open("input.txt", mode='r')

max_pos = 0
positions = []

for pos in f.read().split(','):
    max_pos = max(max_pos, int(pos))
    
    positions.append(int(pos))

f.close()

min_cost = (max_pos * len(positions)) ** 2

print(min_cost, max_pos)

# there's a nicer way of diong this using graph edges but this is good enough

precomp_energy = []

for i in range(max_pos + 1):
    precomp_energy.append(0)

    for j in range(i + 1):
        precomp_energy[i] += j

# rate positions
for final_pos in range(max_pos):
    cost = 0

    for pos in positions:
        cost += precomp_energy[abs(final_pos - pos)]
    
    min_cost = cost if cost < min_cost else min_cost

print("minimal cost:", min_cost)