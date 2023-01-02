inputFile = open("advent-of-code-2015-inputs/input_01.txt", "r")
inputDat = list(inputFile.readlines()[0].strip())
inputFile.close()

floor = 0
for l in inputDat:
    if(l == "("):
        floor += 1
    elif(l == ")"):
        floor -= 1

print(floor)
