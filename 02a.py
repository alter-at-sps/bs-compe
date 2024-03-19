f = open("input.txt", mode='r')

current_max = 0
current_sum = 0

for line in f:
    if line == "\n":
        current_max = current_sum if current_sum > current_max else current_max
        
        current_sum = 0
        continue
    
    current_sum += int(line)

f.close()

print("max group: ", current_max)