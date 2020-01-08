
def subarraySort(array):
    min_oo = float("inf")
    max_oo= float("-inf")

    for i in range(len(array)):
        if i == 0:
            continue
        #check order
        if array[i] < array[i-1]:
            #the two are out of order
            max_oo = max(max_oo, array[i], array[i-1])
            min_oo = min(min_oo, array[i], array[i-1])
    
    if max_oo == float("-inf"):
        return [-1,1]
    max_idx = len(array)-1
    for i, num in enumerate(reversed(array)):
        if num < max_oo:
            max_idx = max_idx - i
    
    min_idx = 0:
    for i, num in enumerate(array):
        if num > min_oo:
            min_idx = min_idx + i
    return [min_idx, max_idx]