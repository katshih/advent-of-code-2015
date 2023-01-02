import hashlib

inputFile = open("advent-of-code-2015-inputs/input_04.txt", "r")
inputDat = inputFile.readlines()[0].strip()
inputFile.close()

#key = "abcdef"
#key = "pqrstuv"
key = inputDat

intFound = False
int = 1

while(not intFound):
    string = key + str(int)
    encoded = hashlib.md5(string.encode('utf-8')).hexdigest()
    if(encoded[0:5] == "00000"):
        intFound = True
    else:
        int += 1

print(int)
print(hashlib.md5((key + str(int)).encode('utf-8')).hexdigest())
