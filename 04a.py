f = open("input-04.txt", mode='r')

values = []

for char in f.read():
    if char == '\n':
        continue

    values.append(int(char))

f.close()

print(values)

matching_sum = 0

for i, v in enumerate(values):
    if v == values[(i + 1) % len(values)]:
        matching_sum += v

print("matching sum:", matching_sum)