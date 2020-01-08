
def shiftedBinarySearch(array, target):
    l = 0
    r = len(array)-1

    if array[l] == target:
        return l
    if array[r] == target:
        return r
    idx = l + ((r-l)//2)
    while array[idx] != target:
        
        if l+1 == r:
            return -1
        #is left side in order
        if array[l] <= array[idx]:
            #if is ordered see if target is in that side
            if target < array[idx] and target > array[l]:
                r = idx
            else:
                l = idx
        else:
        # l is larger then mid so shift has happend there
            if target > array[l] or target < array[idx]:
                r = idx
            else:
                l = idx
        idx = l + ((r-l)//2)
    return idx
    
if __name__ == "__main__":
    a = [111,1,5,23]
    target = 5
    answer = shiftedBinarySearch(a, target)
    print(answer)


    
    # [2,3,4,1,1,1,1]
    
    # search 3

    # l = 3 (4)

