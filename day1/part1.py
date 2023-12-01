def first_last_digit(line:str):
    first_digit = 0
    last_digit = 0
    # Loop forward then break
    for c in line:
        if str.isdigit(c):
            first_digit = c
            break
    # Loop backwards then break
    for i in range(len(line)-1,-1,-1):
        if str.isdigit(line[i]):
            last_digit = line[i]
            break
    return int(str(first_digit) + str(last_digit))

# Open file
total = 0
f = open("input.txt", "r")

for l in f:
    total += first_last_digit(l)

f.close()
    
print(total)
