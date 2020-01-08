

#O(width + depth) time | O(1) space
def searchInSortedMatrix(matrix, target):
    #start in the top right
    row = 0
    col = len(matrix[row])-1

    while True:
        if row == len(matrix) or col <0:
            return False 
        if matrix[row][col] == target:
            return True
        elif target < matrix[row][col]:
            col -= 1
        else:
            row += 1
        

