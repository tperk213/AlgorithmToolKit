def minNumberOfCoinsForChange(n, denoms):
	#set
    if n == 0 :
        return 0
    denoms.sort()
    smallest_num_coins = {}	    
    for key in range(1, n+1):
        smallest_num_coins[key] = float("inf")
    for denom in denoms:
        for key, val in smallest_num_coins.items():
            #edge cases denom = key will be one coin
            if denom == key:
                smallest_num_coins[key] = 1
            if denom < key:
                if key%denom == 0:
                    smallest_num_coins[key] = key/denom 
                else:
                    smallest_num_coins[key] = min(smallest_num_coins[key], (key//denom + smallest_num_coins[key%denom]))
    if smallest_num_coins[n] == float("inf"):
        return -1
    else:
        return int(smallest_num_coins[n])

if __name__ == "__main__":
    x = minNumberOfCoinsForChange(4, [1,5,10])
    print(x)
    # Write your code here.

	# so its ways[key] = min( ways[key - denom

    #case
    #key = denom, ways[key] = 1
	# if key//deonom > 0
	# ways[key] = min(key//denom + ways[key%denom], ways[key])
	
# 	4[1,3,4,5]
# 1	1 1 
# 2	2 1 
# 3	3 2
# 4	4 2
# 5	
# 6	6  
# 7	    2 
# 8	
# 9	
# ..
# n

# 9 [3,4,5]ans 2

# smc 
#       3
# 0 0   0  0
# 1 inf infinf
# 2 inf infinf
# 3 inf 1  1
# 4 inf inf
# 5 inf inf
# 6 inf 2
# 7 inf inf
# 8 inf inf
# 9 inf 3

# curmin = inf