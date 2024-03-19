f = open("input.txt", mode='r')

win_matrix = [
    [ 3, 0, 6 ],
    [ 6, 3, 0 ],
    [ 0, 6, 3 ],
]

score = 0

for line in f:
    if "A" in line:
        p1_index = 0
    elif "B" in line:
        p1_index = 1
    elif "C" in line:
        p1_index = 2
    
    if "X" in line:
        p2_index = 0
    elif "Y" in line:
        p2_index = 1
    elif "Z" in line:
        p2_index = 2
    
    score += p2_index + 1
    score += win_matrix[p2_index][p1_index]

f.close()

print("total score:", score)