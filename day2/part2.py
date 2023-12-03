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

    red = 0
    green = 0
    blue = 0

    # Loop through each pull
    for pull in split2:
        # R : G : B
        cubes = pull.split(",")
        # Loop through each cube
        for c in cubes:
            # empty : size : colour
            cube = c.split(" ")
            if cube[2].strip('\n') == "red":
                if int(cube[1]) > red:
                    red = int(cube[1])
            elif cube[2].strip('\n') == "green":
                if int(cube[1]) > green:
                    green = int(cube[1])
            elif cube[2].strip('\n') == "blue":
                if int(cube[1]) > blue:
                    blue = int(cube[1])
    total += (red * green * blue)

print(total)
        
