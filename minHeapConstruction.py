
# Heap
# A min heap is a balanced tree structure that has the characteristics of right child is larger then left child 
# and root node is the smallest value in the heap
# but not everything to left\right is smaller\larger like a binary tree
# this allows for the heap to be represented as an array
#
#eg 
# [1,4, 5, 55, 60, 8, 22]
#            1
#         4     5
#       55 60  8 22
#
#   parent node is floor(i-1/2)
#   left child node is i*2 + 1
#   right child node is i*2 + 2


class MinHeap():

    def __init__(self, array):
        #self.heap = self.buildHeap(array)
        self.heap = []
        self.buildHeap(array)

    def buildHeap(self, array):
        self.heap = array
        first_parent_idx = (len(array)-2)//2
        for index in reversed(range(first_parent_idx + 1)):
            self.siftDown(index)
        
        
    def siftDown(self, index):
        # swap parent with lowest child then keep shifting down whilst children
        child_l = index * 2 + 1
        while child_l < len(self.heap):
            child_r = index * 2 +2
            if child_r < len(self.heap) and self.heap[child_r] < self.heap[child_l]:
                child_to_swap = child_r
            else:
                child_to_swap = child_l
            
            if self.heap[child_to_swap] < self.heap[index]:
                #swap
                temp = self.heap[index]
                self.heap[index] = self.heap[child_to_swap]
                self.heap[child_to_swap] = temp
                index = child_to_swap
                child_l = index * 2 + 1
            else:
                return
        

    def siftUp(self, index):
        while index > 0:
            parent = (index - 1)//2
            if self.heap[parent] > self.heap[index]:
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            else:
                return
         
    def peek(self):
        pass
    def remove(self, index):
        self.heap[index] = self.heap[len(self.heap)-1]
        self.heap = self.heap[:-1]
        self.siftDown(index)
    def insert(self, val):
        self.heap.append(val)
        self.siftUp(len(self.heap)-1)


def test1():
    array = [3,2,1,40,52,5,2]
    heap = MinHeap(array)
    heap.siftDown(0)
    return heap
if __name__ == "__main__":
    heap = test1()
    print("done")