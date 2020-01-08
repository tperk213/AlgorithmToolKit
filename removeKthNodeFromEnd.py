
class LinkedList():
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def constructFromArray(array):
        first = LinkedList(array[0])
        node = first
        for val in array[1:]:
            node.next = LinkedList(val)
            node = node.next
        return first

def removeKthNodeFromEnd(head, k):
    node = head
    parent = None

    list_len = 1
    for i in range(k-1):
        list_len +=1
        node=node.next 
    
    if node.next == None:
        head = head.next 
        return head 
    
    while node.next != None:
        if parent == None:
            parent = head
        else:
            parent = parent.next 
        node = node.next 
        list_len +=1
    #case where k is 1 
    if list_len == k:
        parent = head
    if k == 1:
        parent.next = None
    else:
        parent.next = parent.next.next
    return head

if __name__ == "__main__":
    a = [0,1,2,3,4,5,6,7,8,9]
    b = LinkedList.constructFromArray(a)
    b = removeKthNodeFromEnd(b,10)
    print("")

    