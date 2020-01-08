from queue import Queue

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self
    
    #use a que to keep track of the order in which to add more children to the que
    def breadthFirstSearch(self, array):
        #add self first
        q = Queue()
        q.put(self)
        while q.empty() is False:
            cur_node = q.get()
            for child in cur_node.children:
                q.put(child)
            array.append(cur_node.name)
        return array

if __name__ == "__main__":
    gr = Node("A").addChild("B").addChild("B").addChild("B")
    a = gr.breadthFirstSearch([])
    print(a)