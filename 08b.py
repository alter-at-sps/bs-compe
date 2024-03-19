f = open("input.txt", mode='r')

tool_matrix = [
    [ 2, 0, 1 ],
    [ 0, 1, 2 ],
    [ 1, 2, 0 ],
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
        win_index = 0
    elif "Y" in line:
        win_index = 1
    elif "Z" in line:
        win_index = 2
    
    score += win_index * 3
    score += tool_matrix[win_index][p1_index] + 1

f.close()

print("total score:", score)