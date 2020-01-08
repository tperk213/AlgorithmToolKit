#Dynamic programing ways of doing something with an array
#for each denom subtract denom from key if above zero there are new way to make change for
# key amount using this denom. the extra ways are amount of ways to make left over from key - denom
#Time O(n + nd) so O(nd)
#space O(n) for hash table of ways to make smaller change
def numberOfWaysToMakeChange(n, denoms):
    #setup of ways hash table init to all 0
    ways = {0: 1}
    for key in range(1,n+1):
        ways[key] = 0
    
    for num in denoms:
        for key, val in ways.items():
            if key - num >= 0:
                ways[key] += ways[key-num]
    return ways[n] 



# 0 1 1 1
# 1 0 1 1
# 2 0 1 1
# 3 0 1 1
# 4 0 1 1
# 5 0 1 2
# 6 0 1 2
