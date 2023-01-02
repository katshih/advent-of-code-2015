inputFile = open("advent-of-code-2015-inputs/input_02.txt", "r")
inputDat = inputFile.readlines()
inputFile.close()

paperSum = 0

for l in inputDat:
    dims = [int(x) for x in l.strip().split('x')]
    sides = [dims[0]*dims[1], dims[1]*dims[2], dims[2]*dims[0]]
    paperSum += 2*sum(sides) + min(sides)

print(paperSum)
