# Constants
max_red = 12
max_green = 13
max_blue = 14
max_cubes = max_red + max_green + max_blue

total = 0

f = open("input.txt", "r")

for line in f:
    
    # Game number : cubes
    split1 = line.split(":")
    # "Game" : num
    game_num = split1[0].split(" ")
    # pull_1 : pull_2 : pull_3
    split2 = split1[1].split(";")

    valid = False

    # Loop through each pull
    for pull in split2:
        red = 0
        green = 0
        blue = 0
        # R : G : B
        cubes = pull.split(",")
        # Loop through each cube
        for c in cubes:
            # empty : size : colour
            cube = c.split(" ")
            if cube[2].strip('\n') == "red":
                red = int(cube[1])
            elif cube[2].strip('\n') == "green":
                green = int(cube[1])
            elif cube[2].strip('\n') == "blue":
                blue = int(cube[1])
        # check if the game was valid
        if red <= max_red and green <= max_green and blue <= max_blue and sum([red,green,blue]) <= max_cubes:    
            valid = True
        else:
            valid = False
            break
    if valid:
        total += int(game_num[1])

print(total)
        
