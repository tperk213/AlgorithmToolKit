
def palindromePartitioningMinCuts(string):
    #Construct table of is palindrome
    # use diagonal increments and check the last and first letter if equal check the table for letters inbetween
    # this alows for a dynamic aproach no is palindome function required
    isPalindrome = [[False for i in string]for j in string]
    for i in range(len(string)):
        isPalindrome[i][i] = True
    i = 1
    while i < len(string):
        j = 0 
        while j < i:
            if string[i] == string[j]:
                if j < i-1: #len of 2 or more
                    if isPalindrome[i-1][j+1]:
                        isPalindrome[i][j] = True
                else:
                    isPalindrome[i][j] = True
            j += 1
        i+=1 
    # loop through letters and calculate cuts
    # calculate cuts by storing in array and loop letters before letter
    # if same check palindrome table if true cuts = letter before + 1
    cuts = [0 for i in range(len(string)+1)]
    cuts[0] = -1
    for i in range(1,len(string)):
        j = 0
        while j < i:
            if isPalindrome[i][j]:               
                cuts[i+1] = cuts[j] + 1
                break
            j += 1
            if j == i:
                cuts[i+1] = cuts[i] + 1
    return cuts[-1]















# def parlindromPartioningMinCuts(string):
#     palindromes = [[False for i in string] for j in string]

#     #handle the diagnal
#     for i in range(len(string)):
#         palindromes[i][i] = True
    
#     for length in range(2, len(string)+1):
#         for i in range(0, len(string) - length +1):
#             j = i + length -1
#             if length == 2:
#                 palindromes[i][j] = string[i] == string[j]
#             else:
#                 palindromes[i][j] = string[i] == string[j] and palindromes[i+1][j-1]
#     cuts = [float("inf") for i in string]
#     for i in range(len(string)):
#         if palindromes[0][i]:
#             cuts[i] = 0
#         else:
#             cuts[i] = cuts[i - 1] +1
#             for j in range(1, i):
#                 if palindromes[j][i] and cuts[j-1] +1 < cuts[i]:
#                     cuts[i] = cuts[j-1] + 1
#     return cuts[-1]



if __name__ == "__main__":
    st = "noonabbad"
    k = palindromePartitioningMinCuts(st)
    print(k)



    