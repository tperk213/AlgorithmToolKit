#Time is O(n^2) hard to workout
#   for loop repeats n-2 times
#   (n-2)sum((n-3) + (n-4) (+ n-5))
#   (n-2)n(3+4+5+..n)
#   below n^3 though
#Space below (n/3)
def threeNumberSum(array, targetSum):
    array = sorted(array)
    return_array = []
    for i, num in enumerate(array):
        left = i + 1
        right = len(array) - 1
        while left != right and left < right:
            complete_sum = (num + array[left] + array[right])
            if targetSum == complete_sum:
                return_array.append([num, array[left], array[right]])
                left += 1
                right -= 1
            elif targetSum < complete_sum:
                right -=1
            else:
                left +=1
    return return_array
