
# essentially orders blocks on max distance to all reqs and return smallest
def apartmentHunting(blocks, reqs):
    #precompute
    distances = {req : [0 for i in range(len(blocks))] for req in reqs}
    for req in reqs:
        distances[req] = findDistances(blocks, req)
    
    #find the best block to live on
    bestDistance = [0, float("inf")]
    for i in range(len(blocks)):
        currentMax = float("-inf")
        for req in reqs:
            currentMax = max(distances[req][i], currentMax)
        if currentMax < bestDistance[1]:
            bestDistance[0] = i
            bestDistance[1] = currentMax
    
    return bestDistance[0]

#returns an array of distance to the closest facility
# Time O(N) runs through the blocks array twice
# Space O(N) returns array of len(blocks)     
def findDistances(blocks, facility):
    distances = []
    distance = float("inf")
    for i in range(len(blocks)):
        if blocks[i][facility] is True:
            distance = 0
        else:
            if distance != float("inf"):
                distance += 1
        distances.append(distance)
    
    distance = float("inf")
    for i in reversed(range(len(blocks))):
        if blocks[i][facility] is True:
            distance = 0
        else:
            if distance != float("inf"):
                distance += 1
        distances[i] = min(distances[i], distance)
    return distances
        


#for each block
#for each req
# work out min distance
# take the max assign that to the  block value
# return the smallest block value


if __name__ == "__main__":
    blocks = [
        {
            "gym":False,
            "school":True,
            "store":False,
        },
        {
            "gym":True,
            "school":False,
            "store":False,
        },
        {
            "gym":True,
            "school":True,
            "store":False,
        },
        {
            "gym":False,
            "school":True,
            "store":False,
        },
        {
            "gym":False,
            "school":True,
            "store":True,
        },
    ]
    facilities = ["gym","school","store"]

    apartmentHunting(blocks, ["store","gym"])



    # k= findDistances(blocks, "gym")
    # s = findDistances(blocks,"school")
    # z = findDistances(blocks, "store")
    # print(k)
    # #gym [1,0,0,1,2]
    # #school [0,1,0,0,0]
    # #store [4,3,2,1,0]
