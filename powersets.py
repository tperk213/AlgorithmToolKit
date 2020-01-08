#O(2^n n) time | O(2^n n) Space
def powerset(array):
    #base case
    if len(array) == 0:
        return[[]]
    elif len(array) == 1:
        return [[],[array[0]]]
    else:
        val = array[0]
        new_array = array[1:]
        powersets = powerset(new_array)
        new_powersets = powersets[:]
        for pset in powersets:
            new_powersets.append(pset+[val])
        return new_powersets

def powerset_pointers(array):

if __name__ == "__main__":
    a = []
    b = powerset(a)
    print(b)
