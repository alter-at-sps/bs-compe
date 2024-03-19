f = open("input.txt", mode='r')

value_sum = 0

for line in f:
    value = int(line)

    while True:
        value = value // 3 - 2
        
        if value < 0:
            break
        
        value_sum += value

f.close()

print("total fuel required (including fuel for fuel):", value_sum)