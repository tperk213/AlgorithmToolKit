from queue import Queue


#Time (rc)(4*riverspace) riverspaces are vertices and 4 is edges so (ve)
#O(rc + ve) is is constant and peeky at a node so if its 0 is constant
#boils down to O(N) where n is the total elements for the matrix
#space (rc+ve)
def riverSizes(matrix):
    river_lens = []
    rlen = 0

#loop through positions checking if they are a 1 (start of river)
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1:
                #start found
                rlen, matrix = riverLenSearch(row,col,matrix)
                river_lens.append(rlen)
    return river_lens
            
                
                
def riverLenSearch(row, col, matrix):
    #Breadth first search
    rlen=0
    q = Queue()
    #start node
    q.put([row,col])
    while q.empty() is False:
        node = q.get()
        row = node[0]
        col = node[1]
        if matrix[row][col] == 1:
            #add len to river
            rlen += 1
            # add neighbours to que
            if row > 0:
                #top
                q.put([row-1, col])
            if col > 0:
                #left
                q.put([row, col-1])
            if row < len(matrix)-1:
                #bottom
                q.put([row+1, col])
            if col < len(matrix[row])-1:
                #right
                q.put([row, col+1])
            #mark matrix position as checked
            matrix[row][col] = 0
    return rlen, matrix


#test
if __name__ == "__main__":
    # rivers = [
    #     [1,0,0],
    #     [1,1,0],
    #     [0,0,0]
    # ]
    rivers = [[1]]
    print(riverSizes(rivers))

#when start found
#len == 1
#riv_pos = pos
#clear_pos
#river_continues = True
#while river contiues 
#   find next pos loop 4 places
#       if any 1
            #river continues is true
        #   
        #add count to len of river
        # update marker to new position
        #clear current position of river
# add len to out array
#clear len
# go to nxt position 

#change array value to false so not evaluated





#loop through positions checking if they are a 1 (start of river)
#when start found
#len == 1
#riv_pos = pos
#clear_pos
#river_continues = True
#while river contiues 
#   find next pos loop 4 places
#       if any 1
            #river continues is true
        #   
        #add count to len of river
        # update marker to new position
        #clear current position of river
# add len to out array
#clear len
# go to nxt position 

#change array value to false so not evaluated