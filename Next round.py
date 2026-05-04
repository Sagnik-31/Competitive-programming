n , k = map(int, input().split())
count = 0
for _ in range(n):

    x = map(int, input().split())

    if x >= k:
        count += 1
print(count)
    


