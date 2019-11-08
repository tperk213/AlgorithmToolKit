#Two number sum
#inputs
    # non-empty array of int 
    # int target sum
#purpose
    # if any two numbers in array
    # add to target sum
    # return them in sorted array
#outputs
    #oreder pair of ints
    #empty array

# 3 methods
    #2 loops        slowest
    #hashtable      fastest but takes up most space
    #sortPointers   fast and takes constant space

#Method 1 2 for loops
    # for each val in the array loop through other vals and check if matches target sum
#Time|space
    #O(n^2)|O(1)
    #O(n^2) due to looping over entire array inside a for loop going over entire array
    #space O(1) constant space only local variables


#Method 2 Hash table
    # using a hash table to store the previous numbers
    # loop through array subtract target sum from each num if result in hash table return num and num-tsum
    # if not add num to hash table
#Time|space
    # O(n)|O(n)
    # O(n) because it loops over array but only does a lookup in hashtable which is constant time 
    # space O(n) because we add values to a hash table so in worse case the entire array n
def twoNumberSumHashTable(array, targetSum):
    table = dict()
    for num in array:
        if targetSum-num in table:
            return sorted([num,targetSum-num])
        else:
            table[num] = True
    return []

#Method 3 Sort then pointer traverse
    # sort the array 
    # use two pointers starting at either end of the array
    # while the sum of the two pointer numbers dont equal the target sum and the pointers arnt pointing to the same number
    #   if the sum of the two pointers is is below the target increment lower pointer (this will increase the sum)
    #   if sum is above the target decrement the higher pointer(this will decrease the sum) 
#Time|Space
    #O(nlog(n))|O(1)
    #time is n for looping over each element and log(n) for the initial sorting of the array
def twoNumberSumSortPointers(array, targetSum):
    array = sorted(array)
    pointerRight = len(array) - 1
    pointerLeft = 0
    while ((array[pointerLeft] + array[pointerRight]) != targetSum) and (pointerLeft != pointerRight):
        if array[pointerLeft] + array[pointerRight] < targetSum:
            pointerLeft += 1
        else:
            pointerRight -= 1
    if pointerLeft == pointerRight:
        return []
    else:
        return [array[pointerLeft], array[pointerRight]]


#Questions:

# what are the 3 methods of implementing two number sum?
# what are the advantages/disadvantages of each method of solving two number sum?

