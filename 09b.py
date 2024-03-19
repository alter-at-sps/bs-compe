f = open("input.txt", mode='r')

score = 0

lc = 'abcdefghijklmnopqrstuvwxyz'
uc = 'abcdefghijklmnopqrstuvwxyz'.upper()

triple = []
i = 0

for line in f:
    triple.append(line)

    if not i == 2:
        i += 1
        continue

    i = 0

    # find char

    char = None

    for c in triple[0]:
        if c in triple[1] and c in triple[2]:
            char = c
            break
    
    if char == None:
        print("failed to find a shared char")
    
    # score char
        
    s = lc.find(char) + 1

    if s == 0:
        s = uc.find(char) + 27

    score += s
    print(char, s, score)

    triple.clear()

f.close()

print("score:", score)