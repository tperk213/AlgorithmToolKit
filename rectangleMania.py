
#Time O(n^2)
#Space O(n)

def rectangleMania(coords):
    #put coords in a table
    coordsTable = {}
    for x, y in coords:
        coordString = str(x)+","+str(y)
        coordsTable[coordString] = True
    #ittercoords
    #   foreach other coord check if it is on a right upper diagonal to origional
    #       if so try and find the other points in the table that make square
    #           if found increment rectangle count
    rectangles = 0
    for x, y in coords:
        for x1, y1 in coords:
            if isUpperRight(x,y,x1,y1):
                coord1,coord2 = getOtherCoords(x,y,x1,y1)
                if coord1 in coordsTable and coord2 in coordsTable:
                    rectangles += 1

def isUpperRight(x,y,x1,y1):
    #return boolean in x1,y1 is above to right of x,y
    return x < x1 and y < y1

def getOtherCoords(x,y,x1,y1):
    #return string form of other 2 corners of the rectangle
    coord1 = str(x)+","+str(y1)
    coord2 = str(x1)+","+str(y)
    return coord1, coord2

