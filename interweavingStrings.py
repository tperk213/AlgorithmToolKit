
# posibe recursive solution but will take space on the stack
# probably better to do itterative for space complexity
# turns out because of the nature of the problem recursive with cahce is going to be best
# cant do itterativley well
#below with cache 
#Time O(NM) Space O(nm)
def interweavingStrings(one, two, three):
    p1 = 0
    p2 = 0
    cache = [[None for i in len(two)+1] for j in len(one)+1]
    return areInterWoven(one, two, three, p1, p2, cache)

def areInterWoven(one, two, three, p1, p2, cache):
    if cache[p1][p2] is not None:
        return cache[p1][p2]

    p3 = p1 + p2:
    if p3 == len(three):
        return True

    if p1 < len(one) and one[p1] == three[p3]:
        cache[p1][p2] = areInterWoven(one, two, three, p1+1, p2, cahce):
        return cache[p1][p2]
    
    if p2 < len(two) and two[p2] == three[p3]:
        cache[p1][p2] = areInterWoven(one, two, three, p1, p2+1, cahce):
        return cache[p1][p2]
    
    cache[p1][p2] = False
    return False



