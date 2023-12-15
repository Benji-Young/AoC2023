import string

parts = []

total = 0

symbols = ["!", "£", "$", "%", "^", "&", "*", "(", ")", "?", "/", "#", "~", "@", "'", ";", ":",
           "-", "_", "+", "=", "<", ">", ",", '"', "[", "]", "\\", "`", "{", "}", "|"]

nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

f = open("input.txt", "r")

# Create a x,y grid of characters
for line in f:
    temp = []
    for c in line:
        temp.append(c)
    parts.append(temp)


def add_number(x, y):
    global total
    current_num = ""
    # digits to the right
    for j in range(y, len(parts[x]), 1):
        if parts[x][j] in nums:
            current_num += parts[x][j]
        else:
            break
    if current_num == "":
        # Digits to the left
        for j in range(y, -1, -1):
            if parts[x][j] in nums:
                current_num = parts[x][j] + current_num
            else:
                break
    else:
        # Digits to the left
        for j in range(y - 1, -1, -1):
            if parts[x][j] in nums:
                current_num = parts[x][j] + current_num
            else:
                break

    # print(current_num + " : " + str(y))
    total += int(float(current_num))
    print(f"(x,y) : ({x},{y}) : {current_num}")


added = False
add = False
# Loop through the dataset
for x in range(len(parts)):
    for y in range(len(parts[x])):
        # if number
        if parts[x][y] in nums:
            if not added:
                # Check adjacent coords for symbols
                for i in range(x - 1, x + 2, 1):
                    for j in range(y - 1, y + 2, 1):
                        # print(str(i) + " : " + str(j))
                        if (0 <= i < len(parts)) and (0 <= j < len(parts[x])-1):
                            if parts[i][j] in symbols:
                                # Add the number and set the new x and y values
                                # add_number(x,y)
                                add = True
                if add:
                    add_number(x, y)
                    added = True
                    add = False
        else:
            added = False

print(total)

