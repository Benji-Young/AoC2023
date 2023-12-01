word_nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
help_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

def first_last_digit(line:str):
    first_index = 0
    last_index = 0
    first_digit = 0
    last_digit = 0
    f_word = False
    l_word = False
    
    # Loop forward then break
    for i in range(len(line)):
        if str.isdigit(line[i]):
            first_index = i
            break
    # Loop backwards then break
    for i in range(len(line)-1,-1,-1):
        if str.isdigit(line[i]):
            last_index = i
            break

    # Check for words
    for word in word_nums:
        if word in line:
            if line.find(word) < first_index:
                first_index = line.find(word)
                first_digit = help_dict[word]
                f_word = True
            if line.rfind(word) > last_index:
                last_index = line.rfind(word)
                last_digit = help_dict[word]
                l_word = True

    if not f_word:
        first_digit = line[first_index]
    if not l_word:
        last_digit = line[last_index]
        
    return int(str(first_digit) + str(last_digit))

# Open file
total = 0

f = open("input.txt", "r")
for l in f:
    total += first_last_digit(l)
f.close()

# Output answer
print(total)
