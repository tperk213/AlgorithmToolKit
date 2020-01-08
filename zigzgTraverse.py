


def zigzagTraverse(array):
    
    def down(array, answer, row, col):
        left = True
        while True:
            if row + 1 == len(array):
                #hit bottom side
                left = False
                break
            if col - 1 < 0:
                # hit the top wall
                break
            
            #havn't hit wall so add val to answer
            answer.append(array[row][col])
            row += 1 
            col -= 1
        answer.append(array[row][col])
        if left is True:
            row += 1
        else:
            col += 1
        #reposition for the next down call
        return answer, row, col

    def up(array, answer, row, col):    
        
        top = True
        while True:
            if col + 1 == len(array[row]):
                #hit right side
                top = False
                break
            if row - 1 < 0:
                # hit the top wall
                break
            
            #havn't hit wall so add val to answer
            answer.append(array[row][col])
            row -= 1 
            col += 1
        answer.append(array[row][col])
        if top is True:
            col += 1
        elif row + 1 < len(array):
            row += 1
        #reposition for the next down call
        return answer, row, col

                
    row = 0
    col = 0
    answer = [array[row][col]]
    row += 1
    go_up = True
    #check if have a grid or just a normal array
    if len(array) > 1 and len(array[0]) > 1:
        while True:
            if go_up is True:
                answer, row, col = up(array,answer, row, col)
                go_up = False
            else:
                answer, row, col = down(array,answer, row, col)
                go_up = True
            if row == len(array) - 1 and col == len(array[0])-1:
                #finished
                answer.append(array[row][col])
                break
    elif len(array) == 1: # only 1 row
        answer = array[0]
    else: #only 1 colomn
        answer = []
        for num in array:
            answer.append(num[0])
    return answer
    #start in down mode
    #go up diagonaly
    #when hit top/right move to right/down then go down
    # go down diagonaly
    # when hit leftside/bottom move down or to right then go up





if __name__ == "__main__":


    a = [[1,2,3,4]
        ]
    a2 = zigzagTraverse(a)
    answer = [1,3,2,4,4,5,9,8,6,5,7,3,4,3,12,2]