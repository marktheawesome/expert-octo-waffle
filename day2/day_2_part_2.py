with open("input.txt", "r") as f:
    data = f.readlines()

max_colors ={
    'red': 12,
    'green': 13,
    'blue': 14
}

total = 0
for line in data:
    power = 1
    cubes = []
    for color in max_colors:
        number_color = []
        color_indexes = [i for i in range(len(line)) if line.startswith(color, i)]
        for i in color_indexes:
            number_of_color = line[i-3] + line[i-2]
            number_color.append(int(number_of_color))
        cubes.append(max(number_color))
    for num in cubes:
        power *= num
    total += power
print(total)
