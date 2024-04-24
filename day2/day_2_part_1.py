with open("input.txt", "r") as f:
    data = f.readlines()

max_colors ={
    'red': 12,
    'green': 13,
    'blue': 14
}

total = 0

for line in data:
    possible = True
    for color in max_colors:
        color_indexes = [i for i in range(len(line)) if line.startswith(color, i)]
        for i in color_indexes:
            number_of_color = line[i-3] + line[i-2]
            if int(number_of_color) > max_colors[color]:
                possible = False
                break
    if possible:
        first_index = line.find(' ')+1
        last_index = line.find(':')

        total += int(line[first_index:last_index])
    else:
        possible = True


print(total)