inputFile = open("advent-of-code-2015-inputs/input_03.txt", "r")
inputDat = list(inputFile.readlines()[0].strip())
inputFile.close()

locs = dict()
coords = [0, 0]

locs[tuple(coords)] = 1

for l in inputDat:
    if(l == '^'): coords[1] = coords[1] + 1
    elif(l == 'v'): coords[1] = coords[1] - 1
    elif(l == '>'): coords[0] = coords[0] + 1
    elif(l == '<'): coords[0] = coords[0] - 1
    else: print('error')

    if(tuple(coords) not in locs):
        locs[tuple(coords)] = 1
    else:
        locs[tuple(coords)] += 1

print(len(locs))
