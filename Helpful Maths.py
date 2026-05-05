s = input()

nums = s.split("+")
nums = list(map(int, nums))

nums.sort()

result = '+'.join(map(str, nums))

print(result)