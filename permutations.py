

def getPermutations(array):
    permutations = []
    permutationsHelper(array, [], permutations)
    return permutations

def permutationsHelper(array, currentPermutation, permutations):
    # if array is empty and we have a current permutation
    if not len(array) and len(currentPermutation):
        permutations.append(currentPermutation)
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i+1:]
            newPermutation = currentPermutation + [array[i]]
            permutationsHelper(newArray, newPermutation, permutations)


#[1,2,3]

#curentperm []
#perms []

#newarray = [2,3]
#newPermutation = [1]

#curentperm []
#perms []

#newarray = [3]
#newPermutation = [1,2,3]








#5, 3, 4, 2

#perms(3,4,2)
#   perms (42)
#        (24)
#        (42)
#    (324)
#    (234)
#    (243)
#    (342)
#    (432)
#    (423)
#     