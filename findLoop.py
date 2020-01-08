
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Time O(n) loops through list values once
# Space O(1)

#Math behind algorithm
# Head to loop head = D
# D to first time f and s meet = P
# FS to D = R
# F = D + P
# so 2F = S = 2D+2P
# so to get to head node subtract P from S
# Total len = T = 2D + P
# so R = T - F = 2D + P - (D + P) = D
# so we can reset F to head and increment F and S till they have both traveled D
# and we get the loop head node

def findLoop(head):

    f = head.next
    s = head.next.next

    # increment f 1 and s 2 each time until s catches f
    while s != f:
        f = f.next
        s = s.next.next

    #then reset f to head and increment both by 1 till they meet
    f = head
    while s != f:
        f = f.next
        s = s.next

    return f


if __name__ == "__main__":
    l = LinkedList(4)
