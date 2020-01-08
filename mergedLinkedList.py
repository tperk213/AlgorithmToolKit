
class LinkedList():
    def __init__(self,value):
        self.value = value 
        self.next = None
        
    def addMany(self,array):
        a = self
        for num in array:
            a.next = LinkedList(num)
            a = a.next
        return self

#Time O(n + m)
#Space O(1)
def mergeLinkedLists(headOne, headTwo):
    # iterate through lists and combine into list with the smallest head
    p1 = headOne
    p1Prev = None
    p2 = headTwo
    while p1 is not None and p2 is not None:
        if p1.value < p2.value:
            p1Prev = p1
            p1 = p1.next
        else:
            if p1Prev is not None:
                p1Prev.next = p2
            p1Prev = p2
            p2 = p2.next
            p1Prev.next = p1
    if p1 is None:
        p1Prev.next = p2
    return headOne if headOne.value < headTwo.value else headTwo


if __name__ =="__main__":
    a = [1,1,3,4,5,5,5,5,10]
    b = [1,2,2,5,6,10,10]
    #[1,1,1,2,2,3,4,5,5,5,5,5,6,10,10]
    alist = LinkedList(1).addMany(a)
    blist = LinkedList(1).addMany(b)
    k = mergeLinkedLists(alist,blist)
    print(k)




