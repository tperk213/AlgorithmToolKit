#select the kth smallest element in the array

#Time   worst O(n^2)
#       av    O(n) due to sorting array first time N then 1/2N next time then 1/4N ... series is 2N so N time
#       best  O(n)
#Space  O(1)
def quickselect(array, k):
    return quickSelectHelper(array, 0, len(array)-1, k)
    
def quickSelectHelper(array, startIdx, endIdx, k):
    while True:
        pivot = startIdx
        l = pivot + 1
        r = endIdx
        while l <= r:
            if array[r] < array[pivot] and array[l] > array[pivot]:
                array[r], array[l] = array[l], array[r]
            if array[r] >= array[pivot]:
                r -= 1
            if array[l] <= array[pivot]:
                l += 1
        array[r], array[pivot] = array[pivot], array[r]
        if r == k-1:
            return array[r]
        elif r < k-1:
            startIdx = r + 1
        else:
            endIdx = r-1
