f = open("input.txt", mode='r')

value_sum = 0

for line in f:
    value = int(line)

    value = value // 3 - 2
    value_sum += value

f.close()

print("total fuel required:", value_sum)