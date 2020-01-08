#Time O(s + b)
#Space O(s)
def smallestSubstringContaining(bigString, smallString):
    #make hash table of characters in smallString and their amounts
    smallTable = {}
    for char in smallString:
        if char in smallTable:
            smallTable[char] += 1
        else:
            smallTable[char] = 1
    
    foundChars = {key: 0 for key in smallTable.keys()}
    found = 0
    shortestStartIdx = 0
    shortestEndIdx = 0
    shortestLen = float("inf")
    r = 0
    l = 0

    while r < len(bigString):
        #handle r char
        if bigString[r] in foundChars:
            char = bigString[r]
            foundChars[char] += 1
            if foundChars[char] <= smallTable[char]:
                found += 1
            #handle found all of small string
            if found == len(smallString):
                #found all in string
                #handle l char
                while found == len(smallString):
                    if bigString[l] in foundChars:
                        char = bigString[l]
                        foundChars[char] -= 1
                        if foundChars[char] < smallTable[char]:
                            found -= 1
                    l += 1
                #Save idx positions if shortest
                if r-(l-1) < shortestLen:
                    shortestStartIdx = l-1
                    shortestEndIdx = r
                    shortestLen = r-(l-1)
        r += 1
    if shortestLen == float("inf"):
        return ""
    return bigString[shortestStartIdx:shortestEndIdx+1]

if __name__ == "__main__":
    bigString = "abcd$ef$axb$c$"
    smallString = "$$abf"
    k = smallestSubstringContaining(bigString, smallString)
    print(k)






#pointer that starts at earliest found char


# aabacde

# aac
# notFoundAll = {a: 2}
# charsToGo = len(smallString) 2
# charsIdxTable = {a:[]}
# startIdx = None
# endIdx = None
# Length = None

# for i in range(len(bigString))
#   

# aaba-cde
# aa
# notFoundAll = {a: 0}
# charsToGo = 0
# charsIdxTable = {a:[0,1]}
# startIdx = 0
# endIdx = 1
# Length = 2

#isShorter(charIdxTable, newIndex, char):
#   olLen = charIdxTable[-1] - charIdxTable[0]
#   newLen = newIdx - charIdxTable[1]
#   if newLen <= olLen:
#       if charIdx 
#       charIdx[0] pop
#       charIdxTable[char].append(newIndx)
#        