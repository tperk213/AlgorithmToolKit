

#Time O(n^2) | Space O(n)
def numberOfBinaryTreeTopologies(n):
    configTable = {}
    configTable[0] = 1
    configTable[1] = 1
    configTable[2] = 2
    for i in range(3, n+1):
        configs = 0
        for j in range(0, i):
            configs += configTable[j] * configTable[i-(1+j)]
        configTable[i] = configs
    return configTable[n]


if __name__ == "__main__":
    n = 4
    k = numberOfBinaryTreeTopologies(n)
    print(k)




#     nodes
#         1, 2, 3, 4, 5, 6, 7 ,8 9, 10
# topos   1  2  5



#place one node at the base then there is n-1 configs on the right
#place one node on the left then there is n-2 configs on the right
#place two nodes on the left the there is 2 configs * n-3 configs
#unitl n nodes on left and 0 nodes on right
