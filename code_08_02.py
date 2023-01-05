inputFile = open("advent-of-code-2015-inputs/input_08.txt", "r")
inputDat = inputFile.readlines()
inputFile.close()

totalCodeChars = 0
totalNewChars = 0

for l in inputDat:
    strLit = l.strip()
    #(codeChars, newChars) = (len(strLit), 2)
    newChars = 2
    for c in strLit:
        if((c == "\\") | (c == "\"")):
            newChars += 1
    #totalCodeChars += codeChars
    totalNewChars += newChars

print(totalNewChars)
