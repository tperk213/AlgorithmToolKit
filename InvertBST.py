from queue import Queue


#Time Av|worst: O(n)
#Space worst: O(d^2)
def invertBinaryTree(tree):
    nodes_to_process = Queue()
    nodes_to_process.put(tree)

    while nodes_to_process.empty() is not True:
        current_node = nodes_to_process.get()
        if current_node is not None:
            nodes_to_process.put(current_node.left)
            nodes_to_process.put(current_node.right)
            temp = current_node.left
            current_node.left = current_node.right
            current_node.right = temp

    return tree

#recursive

def invertBinaryTree(tree):
    #base case
    if tree.left is None and tree.right is None:
        return tree
    else:
        if tree.left is not None:
            invertBinaryTree(tree.left)
        if tree.right is not None:
            invertBinaryTree(tree.right)
        temp = tree.right
        tree.right = tree.left
        tree.left = temp
        return tree
