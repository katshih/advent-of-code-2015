inputFile = open("advent-of-code-2015-inputs/input_05.txt", "r")
inputDat = inputFile.readlines()
inputFile.close()

#strings = ["ugknbfddgicrmopn", "aaa", "jchzalrnumimnmhp", "haegwjzuvuyypxyu", "dvszwmarrgswjxmb"]
strings = inputDat

vowels = {"a", "e", "i", "o", "u"}
badStrings = {"ab", "cd", "pq", "xy"}
niceStrings = 0

for s in strings:
    numVowels = 0
    hasDouble = False
    hasBadString = False
    lastChar = ""
    for c in list(s.strip()):
        if(c in vowels):
            numVowels += 1
        if(c == lastChar):
            hasDouble = True
        if((lastChar + c) in badStrings):
            hasBadString = True
            break
        lastChar = c
    if(((hasBadString == False) & (numVowels >= 3)) & (hasDouble == True)):
        niceStrings += 1

print(niceStrings)
