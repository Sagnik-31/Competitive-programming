s = input().strip()
unique_letters = set(s)

if len(unique_letters) %2 != 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")


