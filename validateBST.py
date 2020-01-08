



#recursive implementation
#base case node is None
#time O(nlog(n))
#space O(log(n))
def validateBst(tree):
    #base case 
    if tree is None:
        return True
    #continue if trees below are valid 
    if validateBst(tree.left) and validateBst(tree.right):
        #check condition for Bst if any checks fail return false
        if tree.left is not None:
            if getMaxValue(tree.left) >= tree.value:
                return False
        if tree.right is not None:
            if getMinValue(tree.right) < tree.value:
                return False
        return True 
    else:
        return False

def getMaxValue(tree):
    if tree.right is None:
        return tree.value
    else:
        return getMaxValue(tree.right)

def getMinValue(tree):
    if tree.left is None:
        return tree.value
    else:
        return getMaxValue(tree.left)

# def getMaxValue(tree):
#     while tree.right is not None:
#         tree = tree.right
#     return tree.value

# def getMinValue(tree):
#     while tree.left is not None:
#         tree = tree.left
#     return tree.value


# Better way of doing it

# The trick is to add a min and max value from nodes above as the validation condition
# this means you can traverse each node only once as opposed to all nodes below to find
# min max of branches below for each node
#time O(n)
#space O(d)
def validateBst(tree, val_min = float("-inf"), val_max = float("inf")):
    #base case
    if tree is None:
        return True
    #validate children
    if tree.right is not None:
        if validateBst(tree.right, val_min = tree.value, val_max = val_max) is False:
            return False
    if tree.left is not None:
        if validateBst(tree.left, val_min=val_min, val_max=tree.value) is False:
            return False
    #validate node
    if tree.value >= val_min and tree.value < val_max:
        return True
    else:
        return False

