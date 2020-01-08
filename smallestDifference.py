
def smallestDifference(arrayOne, arrayTwo):
    arrayOne = sorted(arrayOne)
    arrayTwo = sorted(arrayTwo)

    a1 = 0
    a2 = 0

    smallest_difference = arrayOne[a1] - arrayTwo[a2]
    ret_array = [arrayOne[a1], arrayTwo[a2]]
    if smallest_difference == 0:
        return ret_array    

    while a1 != len(arrayOne)-1 and a2 != len(arrayTwo)-1:
        if arrayOne[a1] - arrayTwo[a2] < smallest_difference:
            smallest_difference = arrayOne[a1] - arrayTwo[a2]
            ret_array = [arrayOne[a1], arrayTwo[a2]]
            if smallest_difference == 0:
                break
        if arrayOne[a1] < arrayTwo[a2]:
            if a1 < len(arrayOne)-1:
                a1 += 1
            else:
                break
        else:
            if a2 < len(array)-1:
                a2 += 1
            else:
                break
    return ret_array
            