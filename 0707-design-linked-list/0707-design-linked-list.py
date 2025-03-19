class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        curr = self.head 

        if index<0 or index>=self.size: #last valid index is size-1
            return -1
        else:
            for i in range(0, index):
                curr = curr.next
            return curr.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0, val)
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        curr=self.head
        new_node=ListNode(val)

        if index<0 or index>self.size: 
            return -1
        
        if index==0:
            if self.head:
                new_node.next = self.head
                self.head.prev = new_node
            self.head = new_node
        else:
            for i in range(0, index-1):
                curr = curr.next

            new_node.next = curr.next
            if curr.next:
                curr.next.prev = new_node
            curr.next = new_node
            curr.prev = curr
        self.size+=1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index<0 or index>=self.size:
            return -1
        
        curr = self.head
        if index==0:
            if self.head.next:
                self.head.next.prev = None
            self.head = self.head.next
        else:
            for i in range(0, index-1):
                curr=curr.next
            if curr.next and curr.next.next:
                curr.next.next.prev = curr
            curr.next = curr.next.next

        self.size -=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)