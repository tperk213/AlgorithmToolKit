def maxSumIncreasingSubsequence(array):
    table = {}
    table[array[0]] = [array[0], [array[0]]]
    cur_max = array[0]
    cur_max_sequence = [array[0]]
    for i in range(1, len(array)):
        
        max_not_above_i = float("-inf")
        for j in range(i):
            k = i-(j+1)
            if array[k] < array[i] and array[k] > 0:
                if max_not_above_i == float("-inf"):
                    max_not_above_i = array[k]
                if table[array[k]][0] > table[max_not_above_i][0]:
                    max_not_above_i = array[k] 
        
        if max_not_above_i == float("-inf"):
            mx = array[i]
            sequence = [array[i]]
        else:
            sequence = table[max_not_above_i][1][:]
            sequence.append(array[i])
            mx = table[max_not_above_i][0] + array[i]
        table[array[i]] = [mx, sequence]

        if mx > cur_max:
            cur_max = mx
            cur_max_sequence = sequence
    return [cur_max, cur_max_sequence]
        #loop back through previous numbers


if __name__ == "__main__":
    seq = [10,15,4,5,11,14,31,25,31,23,25,31,50]
    k = maxSumIncreasingSubsequence(seq)
    print(" s ")



