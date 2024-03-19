input_val = 2147483600

bank_note_count = 0

while input_val > 0:
    if input_val >= 5000:
        input_val -= 5000
        bank_note_count += 1
    elif input_val >= 2000:
        input_val -= 2000
        bank_note_count += 1
    elif input_val >= 1000:
        input_val -= 1000
        bank_note_count += 1
    elif input_val >= 500:
        input_val -= 500
        bank_note_count += 1
    elif input_val >= 200:
        input_val -= 200
        bank_note_count += 1
    elif input_val >= 100:
        input_val -= 100
        bank_note_count += 1
    else:
        print("can't split")

print("total number of notes:", bank_note_count)