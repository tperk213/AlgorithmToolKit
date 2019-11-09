#Given a Binary Search Tress and a val
# find the closest value in the BST to the val given


#Method 1
#   Travel down the tree recursivley the side is based on if the target - node val
#   as returning up the tree return the current nod val or the closest in the child which ever is closer to target


#   set the curr_dif to target - root node val
#   closest = node.val
#   closest in child = none
# 
#   if curr_diff is below  0 then then we should explore the left side of the tree
#   if curr_diff is above 0 then we should explore the right side of the tree as target is above current val
#   
#   use recurion to call function on the left or right side determined above
#   base case is the way we want to go(left or right) doesnt exist meaning we are at a leaf node
#       in this case return the leaf node val  
#   store the result of recursion in closest_in_child
#   if abs( of target - closest in child) is smaller then abs current_diff
#       then there is a closer node in the child tree and this should be returned
#   else
#       return this node val
 

