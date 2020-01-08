
def underscorifySubstring(string, substring):
        

#Time O(N+M) for find
#       
def findLocals(string, substring):
        locations = []
        i = 0
        while True:
                start = string[i].find(substring)
                if start == -1:
                        break
                end = start + len(substring)
                locations.append([start,end])
                i = start+1
        return locations
