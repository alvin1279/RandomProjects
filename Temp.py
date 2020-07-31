from collections import defaultdict

# Processing String
string = "This is the string"
string = string.replace(" ", "").lower()

# Counting Character
letter_count = defaultdict(int)
for letter in string:
    letter_count[letter] += 1

# Printing Character
for letter in sorted(letter_count):
    print(f'{letter}{letter_count[letter]}', end='\t')
