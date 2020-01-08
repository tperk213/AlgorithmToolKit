
def minNumberOfJumps(array):
    curRange = 1
    mpr = 0
    jumps = -1
    for i, num in enumerate(array):
        curRange -= 1
        mpr = max(mpr, num-curRange)
        if curRange == 0:
            jumps += 1
            curRange = mpr
            mpr = 0 
    
    return jumps

#Time O(n) |space O(1)
def minNumberOfJumps(array):
    if len(array) == 1:
		return 0
	steps = array[0]
    mpr = array[0]
    jumps = 0
    for i in range(1,len(array)-1):
		steps -= 1
        mpr = max(mpr, i + array[i])
        if steps == 0:
            jumps += 1
            steps = mpr - i 
    return jumps + 1

if __name__ == "__main__":
    a =[3,4,2,1,2,3,7,1,1,1,3]
    k = minNumberOfJumps(a)
    print(a)





# [3,4,2,1,2,3,7,1,1,1,3]
`  3,5,5,5,5,7,13,13
           1,2,1,0
           1,2
# #curRange
# #MaxPotentialRange = max(curRange + array[i], MaxPotentialRange) 
# #
# mpr = 0, 2, 1, 1,  
# curRange = 0, 3, 2, 1, 0 

# @ this point take the 2 jump (4)
# mpr = 0, 1, 3
# curRange = 2, 1, 0

# @ this point take the 3 jump(3)
# mpr = 0, 5, 0, 1
# curRange = 3, 2, 1, 0
# take the 5 jump (7)
