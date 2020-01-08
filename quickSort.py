
#Time best,average O(Nlog(N)) | worst O(N^2)
#Space O(log(n))

def quickSort(array):
    return quickSortHelper(array, 0, len(array)-1)

def quickSortHelper(array, startIdx, endIndx):
    # base case l and r are same (array of len 1)
    if startIdx >= endIndx:
        return
    pivot = startIdx
    l = startIdx + 1
    r = endIndx

    while l <= r:
        #swap case
        if array[l] > array[pivot] and array[r] < array[pivot]:
            array[l], array[r] = array[r], array[l]
        if array[l] <= array[pivot]:
            l +=1
        if array[r] >= array[pivot]:
            r -= 1
     # when l goes past r
    array[pivot], array[r] = array[r], array[pivot]

    leftSubarrayIsSmaller = r - 1 - startIdx < endIndx - ( r +1 )

    if leftSubarrayIsSmaller:
        array = quickSortHelper(array, startIdx, r-1)
        array = quickSortHelper(array, r+1, endIndx)
    else:
        array = quickSortHelper(array, r+1, endIndx)
        array = quickSortHelper(array, startIdx, r-1)   
    return array
        
