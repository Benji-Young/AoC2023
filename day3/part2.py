import string

parts = []

total = 0

symbols = ["*"]

nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

f = open("input.txt", "r")

# Create a x,y grid of characters
for line in f:
    temp = []
    for c in line:
        temp.append(c)
    parts.append(temp)


def get_number(x, y):
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

    #print(f"(x,y) : ({x},{y}) : {current_num}")
    return current_num


# Loop through the dataset
for x in range(len(parts)):
    for y in range(len(parts[x])):
        adj_nums = []
        # if number
        if parts[x][y] in symbols:
            # Check adjacent coords for numbers
            for i in range(x - 1, x + 2, 1):
                for j in range(y - 1, y + 2, 1):
                    if (0 <= i < len(parts)) and (0 <= j < len(parts[x])-1):
                        if parts[i][j] in nums:
                            new_num = get_number(i, j)
                            if new_num not in adj_nums:
                                adj_nums.append(get_number(i, j))
        if len(adj_nums) == 2:
            print(adj_nums)
            total += int(adj_nums[0]) * int(adj_nums[1])

print(total)

