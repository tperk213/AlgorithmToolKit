
def diskStacking(array):
    array = sorted(array, key=lambda x:x[2])
    table = {str(array[0]):[array[0][2],None]}
    current_max = 0
    current_max_bottom = None
    for i in range(1,len(array)):
        table[str(array[i])] = [array[i][2],None]
        for j in range(i):
            if array[j][0] < array[i][0] and array[j][1] < array[i][1]:
                if table[str(array[j])][0] + array[i][2] > table[str(array[i])][0]:
                    table[str(array[i])] = [table[str(array[j])][0]+array[i][2], array[j]]
        if table[str(array[i])][0] > current_max:
            current_max = table[str(array[i])][0]
            current_max_bottom = array[i]
    disks = [current_max_bottom]
    while True:
        if table[str(current_max_bottom)][1] == None:
            break
        else:
            current_max_bottom = table[str(current_max_bottom)][1]
            disks.append(current_max_bottom)
    return list(reversed(disks))


if __name__ == "__main__":
    d = [[2,1,2], [3,2,3], [2,2,8], [2,3,4], [1,3,1], [4,4,5]]
    k = diskStacking(d)
    print(k)



# [[2,1,2], [3,2,3], [2,2,8], [2,3,4], [1,3,1], [4,4,5]]
# out [[2,1,2], [3,2,3],[4,4,5]]


# for each disks what is the tallest stack that can go on top of it
# order in terms of hight

#         [1,3,1], [2,1,2], [3,2,3], [2,3,4], [4,4,5], [2,2,8]
# [1,3,1]   1        1         1        1        1        1

# [2,1,2]   2        2         2        2        2        2 

# [3,2,3]   3        5         5        5        5        5 

# [2,3,4]   4        4         4        4        4        4 

# [4,4,5]   6        7         10       10       10       10

# [2,2,8]   


# table {
#     [1,3,1] : [1, None]
#     [2,1,2] : [2, None]
#     [3,2,3] : [5, [2,1,2]]
#     [2,3,4] : [4, None]
#     [4,4,5] : [10, [3,2,3]]
#     [2,2,8] : [8, None] 
# }



# for each disk before