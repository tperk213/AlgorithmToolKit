#returns the smallest ammount of changes to go from str1 to str2
def levenshteinDistance(str1, str2):
    #setup
    if len(str1) <= len(str2):
        long_str = str2
        shrt_str = str1
    else:
        long_str = str1
        shrt_str = str2 
    
    prev_row = []
    for i in range(len(shrt_str)+1):
        prev_row.append(i)

    row = []
    i = 1
    for val_l in long_str:
        row.append(i)
        i += 1
        for c, val_s in enumerate(shrt_str):
            c += 1
            if val_l == val_s:
                row.append(prev_row[c-1])
            else:
                row.append(min([prev_row[c-1],prev_row[c],row[-1]])+1)
        prev_row = row
        row = []
    return prev_row[-1]











#table
    lngstr2 
str1   "" y a b a                abc
    "" 0  1 2 3 4               0123
                               y1
    a  1  1 1 2 3              a
    b  2  2 2 1 2              b
    c  3  3 3 2 2              a

cases 
    str1[r] == str2[c]
        #nothing has changed so take diagonal back value
        row_prev[c-1]
    str1[r] != str2[c]
        #theres a difference so add one to the smallest way to get either diagonal smaller string or above or left
        row[c] = min([row[c-1],rowprev[c], rowprev[c-1]])
    #save smaller of strings
    # loop the larger cause we need adjancent vals
    #

