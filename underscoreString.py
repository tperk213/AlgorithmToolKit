
def underscorifySubstring(string, substring):
    locations = findLocations(string, substring)
    locations = colapseLocations(locations)
    return underscore(string, locations)


#Time O(N^2+NM) but more nuanced
def findLocations(string, substring):
    locations = []
    i = 0
    while True:
        start = string[i:].find(substring)
        if start == -1:
            break
        start = start + i
        end = start + len(substring)-1
        locations.append([start, end])
        i = start+1
    return locations

#Time O(len(locations))
def colapseLocations(locations):
    if not len(locations):
        return locations
    colapsedLocations = [locations[0]]
    previous = colapsedLocations[0]
    for i in range(1,len(locations)):
        current = locations[i]
        if current[0]-1 <= previous[1]:
            previous[1] = current[1]
        else:
            colapsedLocations.append(current)
            previous = current
    return colapsedLocations

def underscore(string, locations):
    newString = []
    idxOut = 0
    idxIn = 0
    for i in range(len(string)):
        if idxOut < len(locations) and idxIn == 0:
            if i == locations[idxOut][0]:
                newString.append("_")
                idxIn += 1
        newString.append(string[i])
        if idxOut < len(locations) and idxIn == 1:
            if i == locations[idxOut][1]:
                newString.append("_")
                idxOut += 1
                idxIn = 0
    return "".join(newString)

if __name__ == "__main__":
    a = "testhis is a testtest"
    b = underscorifySubstring(a, "test")
    print(b)
