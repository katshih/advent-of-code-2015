inputFile = open("advent-of-code-2015-inputs/input_02.txt", "r")
inputDat = inputFile.readlines()
inputFile.close()

ribbonSum = 0

for l in inputDat:
    dims = [int(x) for x in l.strip().split('x')]
    perims = [dims[0] + dims[1], dims[1] + dims[2], dims[2] + dims[0]]
    vol = dims[0]*dims[1]*dims[2]
    ribbonSum += 2*min(perims) + vol

print(ribbonSum)
