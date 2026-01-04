
import string

letters = dict()

# initializing the dictionary with all letters as keys and zero as values
for c in string.ascii_letters:
    letters[c] = 0

# print(letters)

with open('american-english.txt', 'r') as words:
    for w in words:
        for char in string.ascii_letters:
            letters[char] += w.count(char)

print(letters)