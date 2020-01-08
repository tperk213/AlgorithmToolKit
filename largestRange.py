


#loop through adding all numbers to a hashtable (n)
#loop through again exploring the hash table in either dirrection to find range (n) as
#   each element is only visited once
#2 loops so 2N or O(n) time and hashtable so O(n) space
def largestRange(array):
    table = {}
    for ele in array:
        table[ele] = False
    
    longest_range = False
    for ele in array:
        cur_range = [ele, ele]
        # if not visited yet
        if table[ele] is False:
            table[ele] = True
            
            #increase to max in range
            high_id = ele
            while True:
                high_id = high_id + 1
                if high_id in table:
                    if table[high_id] is True:
                        break
                    else:
                        table[high_id] = True
                        cur_range[1] = high_id
                else:
                    break
            #increase to min in range
            low_id = ele
            while True:
                low_id -= 1
                if low_id in table:
                    if table[low_id] is True:
                        break
                    else: 
                        table[low_id] = True
                        cur_range[0] = low_id
                else:
                    break
        if longest_range is False:
            longest_range = cur_range
        elif (cur_range[1] - cur_range[0]) > (longest_range[1] - longest_range[0]):
            longest_range = cur_range 
    return longest_range


if __name__ == "__main__":
    r = [-11, -7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,12]
    k = largestRange(r)
    print(k)