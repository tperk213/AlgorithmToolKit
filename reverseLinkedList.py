
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    last = None
    node = head
    while True:
        temp_next = node.next
        node.next = last
        last = node
        node = temp_next
        if node == None:
            return node    