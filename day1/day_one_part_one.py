
with open("input.txt", "r") as f:
    data = f.readlines()

total = 0

for line in data:
    filtered = filter(str.isnumeric, line)
    nums = ''.join(filtered)
    num = nums[0] + nums[-1]
    total += int(num)
print(total)