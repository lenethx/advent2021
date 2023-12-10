
with open("input.txt") as file:
    data=file.readlines()

idsums = 0

for line in data:
    maxvals = {"red":0, "green":0, "blue":0}
    game_and_data = line.split(":")
    gamenum = int(game_and_data[0].split(" ")[-1])

    subgames = game_and_data[1][:-1].split(";") 
    for subgame in subgames:
        cubes = subgame.split(",")
        for cube in cubes:
            cubedata = cube.split(" ")
            if int(cubedata[1]) > maxvals[cubedata[2]]:
                maxvals[cubedata[2]]=int(cubedata[1])

    idsums += maxvals["red"]*maxvals["green"]*maxvals["blue"]

print(idsums)
