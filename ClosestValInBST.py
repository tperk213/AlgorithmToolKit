#Given a Binary Search Tress and a val
# find the closest value in the BST to the val given


#Method 1
#   Travel down the tree recursivley the side is based on if the target - node val is smaller or largers then 0
#   as returning up the tree return the current nod val or the closest in the child which ever is closer to target

#time
#   Av = O(log(n))
#   worst = O(n) because it could be tree with one branch

#Space
#   recursive
#   same as time
#   O(log(n)) worst O(n)
#   Iterative
#   constant O(1)   


#recursive
def findClosestValueInBst(tree, target):
    # Write your code here.
	closest = tree.value
	current_diff = target - tree.value
	closest_in_child = None
	
	if (current_diff < 0) and (tree.left != None) :
		closest_in_child = findClosestValueInBst(tree.left,target)
	elif current_diff > 0 and (tree.right != None):
		closest_in_child = findClosestValueInBst(tree.right,target)
	else:
		return tree.value
	if abs(target - closest_in_child) < abs(current_diff):
		closest = closest_in_child
	return closest

#itterative