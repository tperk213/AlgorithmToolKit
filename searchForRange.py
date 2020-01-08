def searchForRange(array, target):
    l = 0
    r = len(array)-1
    idx = l+((r-l)//2)
    if array[l] == target:
        idx = l
    if array[r] == target:
        idx = r
    while array[idx] != target:
        if l+1 == r:
            return [-1, -1]
        if array[idx] < target:
            l = idx
        else:
            r=idx
        idx = l+((r-l)//2)
    upper = idx+searchForRangeUpper(array[idx:],target)
    lower = searchForRangeLower(array[:idx+1],target)
    return [lower, upper]

def searchForRangeLower(array, target):
	l = 0
	r = len(array)-1
	
	while r > l+1:
		idx = l+((r-l)//2)
		if array[idx] == target:
			r = idx
		else:
			l = idx
	return r

def searchForRangeUpper(array, target):
	l = 0
	r = len(array)-1
	
	while r > l+1:
		idx = l+((r-l)//2)
		if array[idx] == target:
			l = idx
		else:
			r = idx
	return l

if __name__ == "__main__":
    a = [5,7,7,8,8,10]
    target = 7
    ran = searchForRange(a, target)
    print(ran)