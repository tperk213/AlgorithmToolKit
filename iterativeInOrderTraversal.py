
def iterativeInOrderTraversal(tree, callback):
    previous = None
    current = tree

    while current is not None:
        if previous == None or previous == current.parent:
            #going down branch
            previous = current
            if current.left is None and current.right is None:
                callback(current)
                current = current.parent
            elif current.left is not None:
                current = current.left
            else:
                callback(current)
                current = current.right
        elif previous == current.left:
            previous = current
            callback(current)
            if current.right is not None:
                current = current.right
            else:
                current = current.parent
        else:
            previous = current
            current = current.parent
            
class BST:
    def __init__(self, value):
        self.parent = None
        self.value = value
        self.left = None
        self.right = None
    
    #Time
    #   loops the depth of the tree so
    #   average O(log(n))
    #   worst O(n) (one branch case)
    #Space
    #   O(1)
    def insert (self, value):
        current_node = self
        #loop through nodes finding where to insert value
        while True:
            if value > current_node.value:
                if current_node.right == None:
                    current_node.right = BST(value)
                    current_node.right.parent = current_node
                    break
                current_node = current_node.right
            elif value < current_node.value:
                if current_node.left == None:
                    current_node.left = BST(value)
                    current_node.left.parent = current_node
                    break
                current_node = current_node.left
            else:
                new_bst = BST(value)
                new_bst.right = current_node.right
                current_node.right = new_bst
                current_node.right.parent = current_node
                break
        return self
    
    def contains(self, value):
        current_node = self
        while current_node.value != value:
            if current_node.value < value:
                if current_node.right == None:
                    return False
                else:
                    current_node = current_node.right
            else:
                if current_node.left == None:
                    return False
                else:
                    current_node = current_node.left
        return True

    def remove(self, value, parent = None):
        current_node = self
        while current_node is not None:
            if value < current_node.value:
                parent = current_node
                current_node = current_node.left
        return self

    def find_smallest_to_right(self):
        node = self.right
        while node.left != None:
            node = node.left
        return node

    def find_largest_to_left(self):
        node = self.left
        while node.right != None:
            node = node.right
        return node

if __name__ == "__main__":

    btree = BST(1).insert(2).insert(3).insert(4)
    iterativeInOrderTraversal(btree, print)
    print("done")




