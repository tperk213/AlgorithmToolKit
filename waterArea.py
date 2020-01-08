
def waterArea(array):

# areas = []
    area = 0
    left_edge = array[0]
    right_edge = 0
    potential_area = 0
    cur_neg_area = 0
    cur_width = 0
    for i, val in enumerate(array):
        if val >= left_edge:
            cur_neg_area += right_edge
            potential_area = cur_width * left_edge - cur_neg_area
            area += potential_area
            potential_area = 0
            cur_neg_area = 0
            cur_width = 0
            left_edge = val
            right_edge = 0
            continue
        elif val < left_edge and val > right_edge:
            cur_neg_area += right_edge
            right_edge = val
            ri = i
            potential_area = cur_width * right_edge - cur_neg_area
        elif val == right_edge:
            cur_neg_area += right_edge
            potential_area = cur_width * right_edge - cur_neg_area
            ri = i
        elif val < right_edge:
            cur_neg_area += val
        cur_width += 1
    
    #add last potential area
    area += potential_area
    if array[-1] < right_edge:
        area += waterArea(array[ri:])
    return area

if __name__ =="__main__":
    a = [0,8,0,0,5,0,0,10,0,0,1,5,0,3]
    waterArea(a)
    print("done")

# if val > left side lock in potential area and start again
# else if val > right_edge update potential area 
# if end lock in potential area
# potential_area = cur_width * right_edge - cur_neg_area
# leftEdge = 8
# rightEdge= 5
# cur_neg_area = 5
# cur_width = 2




#[0,8,0,0,5,0,0,10,0,0,1,1,0,3]

# areas = []
# if val > left side lock in potential area and start again
# else if val > right_edge update potential area 
# if end lock in potential area
# potential_area = cur_width * right_edge - cur_neg_area
# leftEdge = 8
# rightEdge= 5
# cur_neg_area = 5
# cur_width = 2


# loop

#  if val is higher then left edgs right edge asigned to val
#     8
#     right edge assigned so add area to areas
#     [[0]] 
#     left edge = right edge
#     right edge = 0
    
#     as going along neg area = columns passed
#     le 8
#     re = 5
