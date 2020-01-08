
#Take a list of numbers and find the smallest amount of ways to split pi so that the 
# splits are in the nubers array

def numbersInPi(pi, numbers):
    splits_table = {str(num):0 for num in numbers}
    pi_str = str(pi)
    numbers_str = [str(x) for x in numbers]
    return minNumberOfSplits(pi_str, numbers_str, splits_table)
    
    #loop through prefixs of num (pi for first)
    # when number is found check if the remainder is in the splits_table
    # recurse on the remainder to calculate min num splits

    #loop through prefixs
    

def minNumberOfSplits(num, numbers, splits_table):
    if num in splits_table:
        return splits_table[num]
    elif len(num) == 1:
        return float("inf") 
    min_splits = float("inf")
    for i in range(1,len(num)):
        split = 1
        pre = num[:i]
        if pre in numbers:
            post = num[i:]
            split += minNumberOfSplits(post, numbers, splits_table) 
            min_splits = min(min_splits, split)
    splits_table[num] = min_splits
    return min_splits



if __name__ == "__main__":
    pi = 3456765
    numbers = [345, 567, 676, 5, 34]
    n = numbersInPi(pi, numbers)
    print(n)


