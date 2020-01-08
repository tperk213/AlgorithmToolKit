
#Time O(N)
#Space O(min(N, alphabet))
def longestSubstringWithoutDuplication(string):
    lastFound = {}
    longestString = ''
    startIdx = 0
    for i in range(len(string)):
        if string[i] is in lastFound:
            startIdx = max(startIdx, lastFound[string[i]]+1)
        
        lastFound[string[i]] = i 
        
        if len(string[startIdx:i+1]) > len(longestString):
            longestString = string[startIdx:i+1]
    return longestString