
#Heap min or max
#can be represented as an array
#to do this child left of node is node idx *2 +1 and child right is nodeIdx *2 +2
#parent is nodeIdx -1 //2
#the min is ontop then its two cildren are large then it all the way down
#it is balanced though
#sift up
#takes a value and compares it too the value above if it is smaller swapvalues and repeat
# sift down takes a value then compares it too the values below swaps with the smallest value and repeats
#sift up and down take log(n) time

#Use this feature to sort an array in Nlog(n) time by sifting to top of min heap or maxheap

#Time O(Nlog(n))
#Space O(n)
def heapSort(array):
    heap = buildMaxHeap(array)
    #sort the heap
    for finalIndex in reversed(range(len(heap))):
        heap[0], heap[finalIndex] = heap[finalIndex], heap[0]
        siftDown(0, finalIndex-1, heap)
    return heap
def buildMaxHeap(array):
    firstParentIndex = (len(array)-2)//2
    for i in reversed(range(firstParentIndex+1)):
        siftDown(i, len(array)-1, array)
    return array
    
def siftDown(idx, finishIdx, array):
    while True:
        child_l = idx*2+1
        child_r = child_l+1
        if child_l > finishIdx:
            return
        else:
            child_to_swap = child_l
        if child_r <= finishIdx:
            if array[child_r] > array[child_l]:
                child_to_swap = child_r
        if array[child_to_swap] > array[idx]:
            array[idx], array[child_to_swap] = array[child_to_swap], array[idx]
            idx = child_to_swap
        else:
            return

if __name__ == "__main__":
    array = [45,3,30,12,2,10,19,7]
    k = heapSort(array)