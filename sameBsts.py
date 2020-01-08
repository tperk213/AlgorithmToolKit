def sameBsts(arrayOne, arrayTwo):
    
    def sameBstsHelper(arrayOne, arrayTwo, bone, btwo, ub, lb):
        
        # check if roots are the same
        if arrayOne[bone] != arrayTwo[btwo]:
            return False
    
        
        #branch right update origional pointers and bounds
        fin_one = False
        new_bone = bone
        while True:
            if new_bone + 1 == len(arrayOne):
                fin_one = True
                break
            new_bone += 1
            if arrayOne[new_bone] >= arrayOne[bone] and arrayOne[new_bone] < ub:
                break
            
        fin_two = False
        new_btwo = btwo
        while True:
            if new_btwo + 1 == len(arrayTwo):
                fin_two = True
                break
            new_btwo += 1
            if arrayTwo[new_btwo] >= arrayTwo[btwo] and arrayTwo[new_btwo] < ub:
                break
            
        #stopping if there is a smaller value only in one branch
        if fin_one is True and fin_two is True:
            fin_right = True
        if fin_one is True or fin_two is True:
            return False
        

        # check sameBSts on right branch
        if fin_right == False:
            if sameBstsHelper(arrayOne, arrayTwo, new_bone, new_btwo, ub, arrayOne[bone]) is False:
                return False
    
        # branch left and update pointers and bounds
        fin_one = False
        new_bone = bone
        while True:
            #at end of array with no more smaller values
            if new_bone + 1 == len(arrayOne):
                fin_one = True
                break
            
            new_bone += 1
            if arrayOne[new_bone] < arrayOne[bone] and arrayOne[new_bone] > lb:
                break
            
        
        fin_two = False
        new_btwo = btwo
        while True:
            if new_btwo + 1 == len(arrayTwo):
                fin_two = True
                break
            new_btwo += 1
            if arrayTwo[new_btwo] < arrayTwo[btwo] and arrayTwo[new_btwo] > lb:
                break
            
        #stopping if there is a smaller value only in one branch
        if fin_one is True and fin_two is True:
            return True
        if fin_one is True or fin_two is True:
            return False
        
        # check sameBSts on left branch #ub when going left is last base
        if sameBstsHelper(arrayOne, arrayTwo, new_bone, new_btwo, arrayOne[bone], lb) is False:
            return False
        
       
        
        return True
    
    lb = float("-inf")
    ub = float("inf")
    bone = 0
    btwo = 0

    return sameBstsHelper(arrayOne, arrayTwo, bone, btwo, ub, lb)



#Time (O(N^2)) due to having to loop through the array to find next smallest index for each value
#Space (d) depth of the tree due to recursive calls sitting on the stack
def sameBsts(arrayOne, arrayTwo):
    lb = float("-inf")
    ub = float("inf")
    bone = 0
    btwo = 0
    return sameBstsHelper(arrayOne, arrayTwo, bone, btwo, ub, lb)
def sameBstsHelper(arrayOne, arrayTwo, baseOne, baseTwo, minVal, maxVal):
    #both finished true if one finished not other return false
    if baseOne == -1 or baseTwo == -1:
        return baseOne == baseTwo
    
    #check base
    if arrayOne[baseOne] != arrayTwo[baseTwo]:
        return False
    
    # get left and right base indexs
    leftBaseIndexOne = getIdOfFirstSmaller(arrayOne, baseOne, minVal)
    leftBaseIndexTwo = getIdOfFirstSmaller(arrayTwo, baseTwo, minVal)
    rightBaseIndexOne = getIdofFirstLarger(arrayOne, baseOne, maxVal)
    rightBaseIndexTwo = getIdofFirstLarger(arrayTwo, baseOne, maxVal)

    currentValue = arrayOne[baseOne]
    leftAreSame = sameBstsHelper(arrayOne, arrayTwo, leftBaseIndexOne, leftBaseIndexTwo, minVal, currentValue)
    rightAreSame = sameBstsHelper(arrayOne, arrayTwo, rightBaseIndexOne, rightBaseIndexTwo, maxVal)
    
def getIdOfFirstSmaller(array, base, minVal):
    for i in range(base+1, len(array)):
        if array[i] < array[base] and array[i]>=minVal:
            return i
    return -1

def getIdOfFirstLarger(array, base, manVal):
    for i in range(base+1, len(array)):
        if array[i] >= array[base] and array[i] < maxVal:
            return i
    return -1
    

if __name__ == "__main__":        
    a=[2,1]
    b=[2,1,0]
    q = sameBsts(a,b)
    print(q)
