inputFile = open("advent-of-code-2015-inputs/input_05.txt", "r")
inputDat = inputFile.readlines()
inputFile.close()

strings = ["qjhvhtzxzqqjkmpb", "xxyxx", "uurcxstgmygtbstg", "ieodomkazucvgmuy"]
#strings = inputDat

niceStrings = 0

for s in strings:
    chars = list(s.strip())
    seenPairs = {(chars[0], chars[1]): 0}
    hasDoublePair = False
    hasSplitPair = False
    for idx, c in enumerate(chars[2:]):
        loc = idx + 2
        if(chars[loc - 2] == c):
            hasSplitPair = True
        if((chars[loc - 1], c) in seenPairs):
            if(seenPairs[(chars[loc - 1], c)] == loc - 2):

    if((hasDoublePair == True) & (hasSplitPair == True):
        niceStrings += 1

print(niceStrings)
