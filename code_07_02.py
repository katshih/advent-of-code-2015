inputFile = open("advent-of-code-2015-inputs/input_07.txt", "r")
inputDat = inputFile.readlines()
inputFile.close()

wires = {}

for l in inputDat:
    input = l.split('->')[0].strip()
    wire = l.split('->')[1].strip()
    wires[wire] = {'input': input}

# operators include: NOT, LSHIFT, RSHIFT, AND, OR
def getWireVal(wireName, wires):
    if(wireName.isnumeric()):
        return int(wireName)

    wireInput = wires[wireName]['input']
    if('value' in wires[wireName]):
        return wires[wireName]['value']

    if(wireInput.isnumeric()):
        wireVal = int(wireInput)
    elif("NOT" in wireInput):
        parent = wireInput.split()[1]
        wireVal = ~getWireVal(parent, wires)
    elif("LSHIFT" in wireInput):
        parent = wireInput.split()[0]
        shiftVal = int(wireInput.split()[2])
        wireVal = getWireVal(parent, wires) << shiftVal
    elif("RSHIFT" in wireInput):
        parent = wireInput.split()[0]
        shiftVal = int(wireInput.split()[2])
        wireVal = getWireVal(parent, wires) >> shiftVal
    elif("AND" in wireInput):
        parent1 = wireInput.split()[0]
        parent2 = wireInput.split()[2]
        wireVal = getWireVal(parent1, wires) & getWireVal(parent2, wires)
    elif("OR" in wireInput):
        parent1 = wireInput.split()[0]
        parent2 = wireInput.split()[2]
        wireVal = getWireVal(parent1, wires) | getWireVal(parent2, wires)
    else:
        wireVal = getWireVal(wireInput, wires)

    if(wireVal < 0):
        wireVal += 65536
    wires[wireName]['value'] = wireVal
    return wireVal

[getWireVal(w, wires) for w in wires]
bVal = wires['a']['value']

# reset
for l in inputDat:
    input = l.split('->')[0].strip()
    wire = l.split('->')[1].strip()
    wires[wire] = {'input': input}

wires['b']['input'] = str(bVal)
[getWireVal(w, wires) for w in wires]
print(wires['a']['value'])
