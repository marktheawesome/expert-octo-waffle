def concat(l):
    a = l[0]
    b = l[-1]
    c = str(a) + str(b)
    return int(c)

text_numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

with open("input.txt", "r") as f:
    data = f.readlines()

total = 0
count = 1
for line in data:
    numbers = [0] * (len(line))

    for num in text_numbers:
        indexes = [i for i in range(len(line)) if line.startswith(num,i)]
        for i in indexes:
            numbers[i] = text_numbers.get(num)

    for i in range(len(line)):
        if line[i].isnumeric():
            numbers[i] = line[i]

    filtered_list = [i for i in numbers if i != 0]

    aaa = concat(filtered_list)
    total += aaa
print(total)