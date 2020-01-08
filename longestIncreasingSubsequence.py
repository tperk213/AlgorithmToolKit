def longestIncreasingSubsequence(array):

    sequenceCounts = [None for num in array]
    indices = [None for x in range(len(array)+1)]
    length = 0
    for i, num in enumerate(array):
        #find max sequence that ends in number lower then 12
        newLength = binarySearch(1, length, indices, array, num)
        sequenceCounts[i] = indices[newLength-1]
        indices[newLength] = i
        length = max(length, newLength)
    return buildSequence(array, indices[length], sequenceCounts)

def binarySearch(startIdx, endIdx, indices, array, num):
    if startIdx > endIdx:
        return startIdx
    middleIdx = (startIdx+endIdx)//2
    if array[indices[middleIdx]] < num:
        startIdx = middleIdx + 1
    else:
        endIdx = middleIdx - 1
    
    return binarySearch(startIdx, endIdx, indices, array, num)

def buildSequence(array, currentIdx, sequenceIdx):
    sequence = []
    while currentIdx is not None:
        sequence.append(array[currentIdx])
        currentIdx = sequenceIdx[currentIdx]
    return list(reversed(sequence))
    

if __name__ == "__main__":
    b = [5,6,7,-24,1,2,3,12]
    a = [5,7,-24,12,10,2,3,12,5,6,35]
    out = longestIncreasingSubsequence(b)
    print(a)
#two arrays
# one has position of next in list
# other has lowest value that can be linked to at that position


#ar[5,6,7,-24,1,10,2,3,12,5,6,35]
#ps 0,1,2  , 3, 4,5,6, 7,8,9,10
#i[None,0]
#i[None,3,1,2]
#i[]
#i
#i
#i
#i
#i
#i
#s[N,0,1,N,N,N,N,N,N,N]
#out [-24,2,3,5,6,35]


