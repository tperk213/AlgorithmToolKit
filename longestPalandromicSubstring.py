#O(n(n-1))|space(n)
def longestPalindromicSubstring(string):

    #loop over each letter with pointers moving out so long as they are same increment
    longest_pal = string[0]
    for i in range(len(string)-2):
        back = i
        forward = i+2
        cur_pal = string[i+1]
       
        if cur_pal == string[forward] and string[forward] != string[back]:
            cur_pal = cur_pal + string[forward]
            forward +=1
        while forward < len(string) and back >= 0 and string[back] == string[forward]:
            cur_pal = string[back]+cur_pal+string[forward]
            forward += 1
            back -= 1
        if len(cur_pal) > len(longest_pal):
            longest_pal = cur_pal
    return longest_pal    


if __name__ == "__main__":
    a = "nokn aa"
    r = longestPalindromicSubstring(a)
    print(r)
        