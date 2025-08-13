# Minimum notes calculation using for loop

amount = int(input("Enter the amount: "))
notes = [2000, 500, 200, 100, 50, 20, 10] 
count = 0

print("Notes needed:")
for note in notes:
    if amount >= note:
        num_notes = amount // note
        count += num_notes
        amount %= note
        print(f"{note} x {num_notes}")

print(f"Total number of notes: {count}")
