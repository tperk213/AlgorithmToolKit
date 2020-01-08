
# def longestCommonSubsequence(str1, str2):
#     sequence = []
    
#     if len(str2) < len(str1):
#         str1, str2 = str2, str1
#     for i in range(len(str1)):
#         sequence.append("")
#     for char2 in str2:
#         i = 0
#         for char1 in str1:
#             if char1 == char2:
#                 sequence[i] += char2
#             else:
#                 if i > 0:
#                     if len(sequence[i]) < len(sequence[i-1]):
#                         sequence[i] = sequence[i-1]
#             i += 1
#     if len(sequence) < 1:
#         return []
#     if sequence[-1] == '':
#         return []
#     return list(sequence[-1])


#Time O(nm * min(n,m)) | Space O(nm * min(n,m))
#nm for the grid search 
# * min(n,m) for array concatenation this isnt contant time like appending it takes time equal to length of arrays being joined
# since we do array concat every step of the grid traverse it is multiplied
def longestCommonSubsequence(str1, str2):
    #initialize 2d array
    #str2 is rows
    #str1 cols
    #   s   t   r   1
    #s
    #t
    #r
    #2
    lcs = [[[] for x in range(len(str1)+1)] for y in range(len(str2)+1)]
    
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            if str2[j-1] == str1[i-1]:
                lcs[i][j] = lcs[i-1][j-1] + [str1[i-1]]
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1], key = len)
    return lcs[-1][-1]

#Time O(nm) | space (O(nm))
#no array concatenation so time complexity is constant each loop, space constant as only 4 entries in array
def longestCommonSubsequence(str1, str2):
    lcs = [[[None, 0, None, None]for x in range(len(str1)+1)] for y in range(len(str2)+1)]

    for i in range(len(str2) + 1):
        for j in range(len(str1)+1):
            if str2[i-1] == str1[j-1]:
                lcs[i][j] = [str2[i-1], lcs[i-1][j-1][1] + 1, i-1, j-1]
            else:
                if lcs[i-1][j][1] > lcs[i][j-1][1]:
                    lcs[i][j] = [None, lcs[i-1][j][1], i-1, j]
                else:
                    lcs[i][j] = [None, lcs[i][j-1][1], i, j-1]
    return buildSequence(lcs)

def buildSequence(lcs):
    sequence = []
    i = len(lcs)-1
    j = len(lcs[0]) -1
    while i != 0 and j != 0:
        current = lcs[i][j]
        if current[0] is not None:
            sequence.append(current[0])
        i = current[2]
        j = current[3]
    return list(reversed(sequence))
    
if __name__ == "__main__":
    str1 = "12345"
    str2 = "1234"
    k = longestCommonSubsequence(str1, str2)
    print("")