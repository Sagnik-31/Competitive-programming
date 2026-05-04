n = int(input())
s = str(n)
c = 0
for el in s:
    if el == '4' or el == '7':
        c += 1 # count number of lucky digits
if c == 4 or c == 7: # check if that equals 4 or 7
    print("YES")
else:
    print("NO")


