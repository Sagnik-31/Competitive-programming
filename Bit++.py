n = int(input())
X = 0
for _ in range(n):

    t = input()

    if t == 'X++' or t == '++X':
        X += 1
    elif t == 'X--' or t == '--X':
        X -= 1

print(X)
    
