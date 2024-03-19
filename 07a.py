f = open("input.txt", mode='r')

max_pos = 0
positions = []

for pos in f.read().split(','):
    max_pos = max(max_pos, int(pos))
    
    positions.append(int(pos))

f.close()

min_cost = max_pos * len(positions)

# there's a nicer way of diong this using graph edges but this is good enough

# rate positions
for final_pos in range(max_pos):
    cost = 0

    for pos in positions:
        cost += abs(final_pos - pos)
    
    min_cost = cost if cost < min_cost else min_cost

print("minimal cost:", min_cost)
