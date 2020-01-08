
def maxPathSum(tree):
    _, a = maxPathHelper(tree)
    return a     

def maxPathHelper(tree)
    
    if tree is None:
        return 0, 0
    
    left_bmx, left_amx = maxPathSum(tree.left)
    right_bmx, right_amx = maxPathSum(tree.right)

    bmx = max(tree.value + left_bmx, tree.value + right_bmx)
    amx = max(bmx, right_amx, left_amx, tree.value + left_bmx + right_bmx)

    return bmx, amx

if __name__ == "__main__":
    
    