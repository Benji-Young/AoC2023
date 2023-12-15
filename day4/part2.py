f = open("input.txt", "r")
arr = f.readlines()
cards = [[1] for x in arr]
total = 0
for i in range(len(arr)):
    card = arr[i].split(":")[1].split("|")
    card[0] = card[0].strip().split()
    card[1] = card[1].strip().split()

    total += cards[i][0]
    while cards[i][0] > 0:
        card_count = 0
        # Check the cards for winning values
        for x in card[1]:
            if x in card[0]:
                card_count += 1
        # Burn card
        cards[i][0] -= 1
        for j in range(i+1, i+(card_count+1), 1):
            cards[j][0] += 1

print(total)
f.close()
