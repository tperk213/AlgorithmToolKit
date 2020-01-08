
def mergeSort(array):
    auxArray = array[0:]
    helperSort(array, auxArray, 0, len(array)-1)

def helperSort(mainArray, auxArray, sp, ep):
    #base case
    if sp == ep:
        return

    
    #devide
    newEp = sp+(ep-sp)//2
    helperSort(auxArray, mainArray, sp, newEp)
    halfp = newEp
    newEp += 1
    helperSort(auxArray, mainArray, newEp, ep)
    #sort
    sortIdx = sp
    while True:
        #make sure ther pointers arnt out of bounds
        if sp > halfp and newEp > ep:
            #done
            break
        elif sp > halfp:
            mainArray[sortIdx] = auxArray[newEp]
            newEp += 1
        elif newEp > ep:
            mainArray[sortIdx] = auxArray[sp]
            sp += 1
        elif auxArray[sp] < auxArray[newEp]:
            mainArray[sortIdx] = auxArray[sp]
            sp += 1
        elif auxArray[sp] > auxArray[newEp]:
            mainArray[sortIdx] = auxArray[newEp]
            newEp += 1
        else:
            mainArray[sortIdx] = auxArray[newEp]
            newEp+=1
            sortIdx+=1
            mainArray[sortIdx] = auxArray[sp]
            sp +=1
        sortIdx+=1

if __name__ == "__main__":
    a = [5,-2,2,-8,3,-10,-6,-1,2,-2,9,1,1]
    mergeSort(a)
    print(a)
    
    
