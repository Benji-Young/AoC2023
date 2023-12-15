f = open("input.txt", "r")
total = 0
arr = f.readlines()
for l in arr:
    card = l.split(":")[1].split("|")
    matches = 0
    card[0] = card[0].strip().split()
    card[1] = card[1].strip().split()
    for x in card[1]:
        if x in card[0]:
            matches += 1
    if matches > 0: total += 2 ** (matches - 1)
print(total)
f.close()
