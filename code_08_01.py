inputFile = open("advent-of-code-2015-inputs/input_08.txt", "r")
inputDat = inputFile.readlines()
inputFile.close()

totalCodeChars = 0
totalValChars = 0

# special chars: \\, \", \x**
for l in inputDat:
    strLit = l.strip()
    (idx, codeChars, valChars) = (1, 1, 0)
    while(idx < len(strLit) - 1):
        if(strLit[idx] == "\\"): # there is one backslash
            if((strLit[idx + 1] == "\\") | (strLit[idx + 1] == "\"")): # \\ or \| found
                idx += 2
                codeChars += 2
                valChars += 1
            elif(strLit[idx + 1] == "x"):
                idx += 4
                codeChars += 4
                valChars += 1
        else:
            idx += 1
            codeChars += 1
            valChars += 1
    codeChars += 1 # get final quote
    if(False):
        print(strLit)
        print(codeChars)
        print(valChars)
    totalCodeChars += codeChars
    totalValChars += valChars

print(totalCodeChars - totalValChars)
