key = input("Enter key (26 letters): ")
text = input("Enter text to encrypt: ")

baseline = "abcdefghijklmnopqrstuvwxyz"
encrypted = ""

# loop through each character in the input text
for i in text:
    lower = i.lower()
    # Find index of baseline
    index = baseline.find(lower)

    letter = i;
    # If it's not in the baseline, don't encrypt it
    if (index != -1) : letter = key[baseline.find(lower)]

    encrypted += letter

print("Encrypted text: " + encrypted)
