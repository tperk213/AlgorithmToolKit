
def patternMatcher(pattern, string):
    flip = False if pattern[0] == 'x' else True
    pattern = getNewPattern(pattern)
    counts, firstY = getCountAndFindYPosition(pattern)
    if counts['y'] > 0:
        for i in range(1,len(string)):
            xlen = i*counts['x']
            if counts['y'] > len(string)-xlen:
                break
            elif (len(string) - xlen)%counts['y'] != 0:
                continue
            ylen = (len(string) - xlen)//counts['y']

            x = string[0:i]
            y = string[i*firstY:(i*firstY)+ylen]
            patternString = ""
            for l in pattern:
                if l == 'x':
                    patternString += x
                else:
                    patternString += y    
            if patternString == string:
                if flip:
                    return [y,x]
                else:
                    return [x,y]
    else:
        for i in range(len(string)):
            if len(string)%i != 0:
                continue
            x = string[0:i]
            patternString = ""
            for j in range(len(pattern)):
                patternString += x
            if patternString == string:
                if flip:
                    return["",x]
                else:
                    return[x,""]
    return []

def getNewPattern(pattern):
    newPattern = []
    if pattern[0] == "x":
        return pattern
    else:
        for i in range(len(pattern)):
            if pattern[i] == 'y':
                newPattern.append('x')
            else:
                newPattern.append('y')
    return "".join(newPattern)

def getCountAndFindYPosition(pattern):
    counts = {'x':0, 'y':0}
    firstY = None
    for i in range(len(pattern)):
        counts[pattern[i]] += 1
        if firstY is None and pattern[i] == 'y':
            firstY = i
    return counts,firstY

if __name__ == "__main__":
    s = "gogopowerrangergogopowerranger"
    pattern = "xxyxxy"
    t = patternMatcher(pattern, s)
    print(t)

    