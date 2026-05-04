s = input()

letters = set()

for ch in s:
    if ch.isalnum():
        letters.add(ch)

print(len(letters))
    