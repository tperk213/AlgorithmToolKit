#Time O(n+m)
#space O(m)
def knuthMorrisPrattAlgorithm(string, substring):
    pattern = buildPattern(substring)
    i = 0
    j = 0
    while i + len(substring) - j <= len(string):
        if string[i] == substring[j]:
            if j == len(substring)-1:
                return True
            j += 1
            i += 1
        elif j > 0:
            j = pattern[j-1] + 1
        else:
            i+=1
    return False


def buildPattern(substring):
    # makes an array of numbers that denote at that position the length of suffix that equals the same length prefix 
    pattern = [-1 for i in substring]
    j = 0
    i = 1
    while i < len(substring):
        if substring[i] == substring[j]:
            pattern[i] = j
            i+=1
            j+=1
        elif j > 0:
            j = pattern[j-1] + 1
        else:
            i+=1
    return pattern







