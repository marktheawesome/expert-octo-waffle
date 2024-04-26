# unitTest.txt outputs
# Part 1: 925
# Part 2: 6756

with open("unitTest.txt", "r") as f:
    data = f.readlines()

total = 0

for i in range(1, len(data) - 1):
    for j in range(len(data[i]) - 1):
        char = data[i][j]
        numbers = []
        if not char.isnumeric() and char != '.': # is special char
            # North Test
            if data[i-1][j].isnumeric():
                number = data[i-1][j]
                if data[i-1][j+1].isnumeric() and data[i-1][j-1].isnumeric():
                    number = data[i-1][j-1:j+2]

                else:
                    if data[i-1][j+1].isnumeric():
                        number = data[i-1][j:j+2]
                        if data[i-1][j+2].isnumeric():
                            number = data[i-1][j:j+3]

                    if data[i-1][j-1].isnumeric():
                        if data[i-1][j-2].isnumeric():
                            number = data[i-1][j-2:j+1]

                print("North: ", number)
                numbers.append(int(number))

            else:
                # NorthEast Test
                if data[i-1][j+1].isnumeric():
                    number = data[i-1][j+1]
                    if data[i-1][j+2].isnumeric():
                        number = data[i-1][j+1:j+3]
                        if data[i-1][j+3].isnumeric():
                            number = data[i-1][j+1:j+4]

                    print("NorthEast: ", number)
                    numbers.append(int(number))

                # NorthWest Test
                if data[i-1][j-1].isnumeric():
                    number = data[i-1][j-1]
                    if data[i-1][j-2].isnumeric():
                        number = data[i-1][j-2:j]
                        if data[i-1][j-3].isnumeric():
                            number = data[i-1][j-3:j]
                    print("NorthWest", number)
                    numbers.append(int(number))

            # South Test
            if data[i+1][j].isnumeric():
                if data[i+1][j+1].isnumeric() and data[i+1][j-1].isnumeric():
                    number = data[i+1][j-1:j+2]
                if data[i+1][j+1].isnumeric():
                    if data[i+1][j+2].isnumeric():
                        number = data[i+1][j:j+3]

                elif data[i+1][j-1].isnumeric():
                    if data[i+1][j-2].isnumeric():
                        number = data[i+1][j-2:j+1]

                    else:
                        number = data[i+1][j-1:j+1]

                print("South: ", number)
                numbers.append(int(number))

            else:
                # SouthWest
                if data[i+1][j-1].isnumeric():
                    number = data[i+1][j-1:j]
                    if data[i+1][j-2].isnumeric():
                        number = data[i+1][j-2:j]
                        if data[i+1][j-3].isnumeric():
                            number = data[i+1][j-3:j]
                    print("SouthWest: ", number)
                    numbers.append(int(number))

                # SouthEast Test
                if data[i+1][j+1].isnumeric():
                    number = data[i+1][j+1]
                    if data[i+1][j+2].isnumeric():
                        number = data[i+1][j+1:j+3]
                        if data[i+1][j+3].isnumeric():
                            number = data[i+1][j+1:j+4]
                    print('SouthEast: ', number)
                    numbers.append(int(number))

            # East Test
            if data[i][j+1].isnumeric():
                number = data[i][j+1]
                if data[i][j+2].isnumeric():
                    number = data[i][j+1:j+3]
                    if data[i][j+3].isnumeric():
                        number = data[i][j+1:j+4]
                print("East: ", number)
                numbers.append(float(number))

            # West Test
            if data[i][j-1].isnumeric():
                number = data[i][j-1]
                if data[i][j-2].isnumeric():
                    number = data[i][j-2:j]
                    if data[i][j-3].isnumeric():
                        number = data[i][j-3:j]
                print("West: ", number)
                numbers.append(int(number))
            total += sum(numbers)

print(total)