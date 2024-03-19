f = open("input.txt", mode='r')

in_str = f.read().strip()

f.close()

unique_string = None
string_loc = 0

for i in range(len(in_str) - 13):
    temp_str = ''
    
    unique = True
    for j in range(14):
        if in_str[i + j] in temp_str:
            unique = False            
            break
        
        temp_str += in_str[i + j]

    if unique:
        unique_string = temp_str
        string_loc = i

        break

if unique_string == None:
    print("failed to find a unique string for of 4 chars")
    exit(-1)

print(f"found unique string \"{unique_string}\" ending at index {string_loc + 14}")