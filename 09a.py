f = open("input.txt", mode='r')

score = 0

lc = 'abcdefghijklmnopqrstuvwxyz'
uc = 'abcdefghijklmnopqrstuvwxyz'.upper()

for line in f:
    p1 = line[:len(line) // 2]
    p2 = line[len(line) // 2:]

    # find char

    char = None

    for c in p1:
        if c in p2:
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

f.close()

print("score:", score)