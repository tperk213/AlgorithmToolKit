
# use dynamic programing which is building up an array to form the solution

# the logic is as new numbers are added to the array what is larger the (n-1) term or the (n-2) + n term
#use two arrays one a running total and the other for the numbers that are needed to make the current largest sum

#time(O(n))
#space(O(1))
def maxSubsetSumNoAdjacent(array):
    #handle first 3 edges case array is below len 3
    if len(array) == 0:
		return 0
	elif len(array) == 1 :
		return array[0]
	elif len(array) == [2]:
		return max(array[0], array[1])
	#setup initials
    else:
		n2 = array[0]
		n1 = max(array[0], array[1])
	#loop through array using max algo
    for val in array[2:]:
		temp = n1
		n1 = max(val + n2, n1)
		n2 = temp
	return n1
