
# def knapsackProblem(items, capacity):
#     caps = {}
#     for i in range(capacity+1):
#         caps[i] = [0,[]]
#     new_items = {val:key for key,val in items}
#     items_to_remove = []
#     largest = [0,[]]
#     for i in range(1, capacity+1):
#         for weight, val in new_items.items():
#             if weight <= i:
#                 #check if value of new items is greater then stored
#                 if val + caps[i-weight][0] > caps[i][0]:
#                     caps[i][0] = val + caps[i-weight][0]
#                     if caps[i-weight] != 0:
#                         caps[i][1] = [caps[i-weight][1][:],[val, weight]]
#                     else:
#                         caps[i][1] = [[val, weight]]
#                     items_to_remove.append(weight)
#                     if caps[i][0] > largest[0]:
#                         largest = caps[i]
#         for weight in items_to_remove:
#             del(new_items[weight])
#         items_to_remove = []
                
#     return largest




# [val, weight]
# []
# table = {
#           0   :   [total val, [[val, weight],[val, weight]]],
#           1,
#           2,
#             3,
#             4,
#             5,
#             ..
# # }

# 1 = [2, [2,1]]
# 3

# if 

def knapsackProblem(items, capacity):
    max_vals = [[0 for i in range(capacity+1)] for j in range(len(items)+1)]
    for j, item in enumerate(items):
        for i in range(1,capacity+1):
            if item[1] <= i:
                max_vals[j+1][i] = max(max_vals[j][i], max_vals[j][i-item[1]]+item[0])
            else:
                max_vals[j+1][i] = max_vals[j][i]
    return buildSequence(max_vals, items)

def buildSequence(max_vals, items):
    val = max_vals[-1][-1]
    return_items = []
    row = len(max_vals)-1
    col = len(max_vals[0])-1
    while max_vals[row][col] != 0:
        if max_vals[row][col] > max_vals[row-1][col]:
            return_items.append(row-1)
            col -= items[row-1][1]
        row -= 1
    return [val, return_items[::-1]]



if __name__ == "__main__":
    items = [
        [1,2],
        [4,3],
        [5,6],
        [6,7]
    ]
    capacity = 10
    l = knapsackProblem(items, capacity)
    print(l)




# knapsackProblem
#      0,1,2,3,4,5,6,7,8,9,10
# []   0 0 0 0 0 0 0 0 0 0 0
# [1,2]0 0 1 1 1 1 1 1 1 1 1
# [4,3]0 0 1 4 4 5 5 5 5 5 5
# [8,4]0 0 1 4 8 8 9 12121313
# [9,5]0 0 1 4 8 9 9 12131717

[9,5], [8,4]
# if wieght is same or larger:
#     fill in with max( row above, row above - weight + val)
# else:
#     fill in with row above
