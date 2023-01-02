import numpy as np
import re

inputFile = open("advent-of-code-2015-inputs/input_06.txt", "r")
inputDat = inputFile.readlines()
inputFile.close()

lightArray = np.zeros((1000, 1000))
#inputDat = ["turn off 499,499 through 500,500"]

for l in inputDat:
    match = re.match(r"(\D*) (\d*),(\d*) through (\d*),(\d*)", l.strip())
    if match:
        instructions = match.groups()
    else:
        print('error')
    if(instructions[0] == "turn off"):
        lightArray[int(instructions[1]):int(instructions[3]) + 1, int(instructions[2]):int(instructions[4]) + 1] -= 1
        lightArray = lightArray.clip(0)
    elif(instructions[0] == "turn on"):
        lightArray[int(instructions[1]):int(instructions[3]) + 1, int(instructions[2]):int(instructions[4]) + 1] += 1
    elif(instructions[0] == "toggle"):
        lightArray[int(instructions[1]):int(instructions[3]) + 1, int(instructions[2]):int(instructions[4]) + 1] += 2
    else:
        print('error')

print(np.sum(lightArray))
