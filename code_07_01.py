inputFile = open("advent-of-code-2015-inputs/input_07_test.txt", "r")
inputDat = inputFile.readlines()
inputFile.close()

wires = {}

for l in inputDat:
    input = l.split('->')[0].strip()
    wire = l.split('->')[1].strip()
    wires[wire] = input

# operators include: AND, OR, LSHIFT, RSHIFT, NOT
def getWireVal(wireName, wires):
    wireInput = wires[wireName]
    if(wireInput.isnumeric()):
        return int(wireInput)
    elif("NOT" in wireInput):
        parent = wireInput.split()[0]
        return ~getWireVal(parent, wires)
