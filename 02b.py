f = open("input.txt", mode='r')

current_max_set = [0]
current_sum = 0

for line in f:
    if line == "\n":
        i = 0
        for max in current_max_set:
            if current_sum > max:
                current_max_set.insert(i, current_sum)
                break

            i += 1
        
        current_sum = 0
        continue
    
    current_sum += int(line)

f.close()

print("max group: ", sum(current_max_set[:3]), current_max_set[:3])