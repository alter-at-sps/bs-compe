input_val = 2147483600

total_length = 0
note_lengths = [
    170,
    164,
    158,
    152,
    146,
    140,
]

while input_val > 0:
    if input_val >= 5000:
        input_val -= 5000
        total_length += note_lengths[0]
    elif input_val >= 2000:
        input_val -= 2000
        total_length += note_lengths[1]
    elif input_val >= 1000:
        input_val -= 1000
        total_length += note_lengths[2]
    elif input_val >= 500:
        input_val -= 500
        total_length += note_lengths[3]
    elif input_val >= 200:
        input_val -= 200
        total_length += note_lengths[4]
    elif input_val >= 100:
        input_val -= 100
        total_length += note_lengths[5]
    else:
        print("can't split")

print("total number of notes:", total_length)