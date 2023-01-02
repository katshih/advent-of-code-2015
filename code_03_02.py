# 2356 too high

inputFile = open("advent-of-code-2015-inputs/input_03.txt", "r")
inputDat = list(inputFile.readlines()[0].strip())
inputFile.close()

#inputDatTest = list("^v^v^v^v^v")

def visitHouses(locs, startCoords, directions):
    coords = [startCoords[0], startCoords[1]]
    for l in directions:
        if(l == '^'): coords[1] = coords[1] + 1
        elif(l == 'v'): coords[1] = coords[1] - 1
        elif(l == '>'): coords[0] = coords[0] + 1
        elif(l == '<'): coords[0] = coords[0] - 1
        else: print('error')

        if(tuple(coords) not in locs):
            locs[tuple(coords)] = 1
        else:
            locs[tuple(coords)] += 1

locs = dict()
startCoords = (0, 0)
locs[startCoords] = 1

santaDat = inputDat[0::2]
roboDat = inputDat[1::2]

visitHouses(locs, startCoords, santaDat)
visitHouses(locs, startCoords, roboDat)

print(len(locs))
