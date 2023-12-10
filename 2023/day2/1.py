
with open("input.txt") as file:
    data=file.readlines()

maxvals = {"red":12, "green":13, "blue":14}
idsums = 0

for line in data:
    game_and_data = line.split(":")
    gamenum = int(game_and_data[0].split(" ")[-1])

    subgames = game_and_data[1][:-1].split(";") 
    possible = True
    for subgame in subgames:
        cubes = subgame.split(",")
        for cube in cubes:
            cubedata = cube.split(" ")
            if int(cubedata[1]) > maxvals[cubedata[2]]:
                possible = False
    if possible:
        idsums += gamenum

print(idsums)
