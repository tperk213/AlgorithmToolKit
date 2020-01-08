#Time O(n*m^2 + nlog(n)) m is len(longest string)n is number of strings
#space O(nm) n enteries in table at worst key will be m len
def longestStringChain(strings):
    #sort strings based on length O(nlog(n))
    strings.sort(key=lambda s: len(s))
    #itter through strings (shortest first)
    #   chainlen=0
    #   itter through letters in string removing each
    #       search table for string 
    #           if found chainlen = max(curlen, table val +1)
    #   table[string] = chainlen
    chainLens = {}
    overAllMax = [float("-inf"), None]
    for string in strings:
        chainLen = 0
        nextString = None
        if len(string) == 1:
            chainLens[string] = [1, None]
        else:
            for i in range(len(string)): # m times
                newString = getNewString(string,i)# m opperation
                if newString in chainLens and chainLens[newString][0] > chainLen:
                    chainLen = chainLens[newString][0]
                    nextString = newString
            chainLens[string] = [chainLen + 1, nextString]
        if chainLens[string][0] > overAllMax[0]:
            overAllMax = [chainLens[string][0], string]
    #construct return string array
    returnList = []
    current = overAllMax
    if current[0]== 1:
        return []
    while current[1] is not None:
        returnList.append(current[1])
        current = chainLens[current[1]]
    return returnList    
    

def getNewString(string, i):
    if i == len(string)-1:
        newString = string[0:i]
    else:
        newString = string[0:i]+string[i+1:]
    return newString

