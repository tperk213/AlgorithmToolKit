
def fourNumberSum(array, targetSum):
    table= {}
    quads = []
    for idx,num1 in enumerate(array):
        #calculate Qs and check for Ps in hashtable
        if idx != len(array)-1:
            for num2 in array[idx+1:]:
                Q = num1 + num2
                if targetSum-Q in table:
                    # add quads for each entry in table
                    for P in table[targetSum-Q]:
                        p1, p2 = P
                        quads.append([num1, num2, p1, p2])
        #calculate Ps and add to table
        for num2 in array[:idx]:
            P = num1 + num2
            if P in table:
                table[P].append([num1,num2])
            else:
                table[P] = [[num1, num2]]
    return quads

if __name__ == "__main__":
    array = [1,2,3,4,5,6,7]
    target = 10
    quads = fourNumberSum(array, target)
    print("done")
