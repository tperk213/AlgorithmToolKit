#Write a Binary search tree class
# important methods

#Insert
#   takes a value and inserts it into the BST at correct position

#Contains
#   returns a bool True if value is contained in BST

#Remove
#   removes a value from the bst



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
#tests insert
# 5,10,4,22,8,1,4

#             5
#         4       10
#     1     4    8    22

#remove
#base case (no parent)
#has both trees and (parrent)
#has only left tree
#has only right tree

def test1():
    test1_bst = BST(5).insert(10).insert(4).insert(22).insert(8).insert(1).insert(4) 
    return test1_bst
if __name__ == "__main__":
    bst1 = test1()
    false1 = bst1.contains(100)
    false2 = bst1.contains(6)
    true1 = bst1.contains(5)
    true2 = bst1.contains(8)
    print("done")



