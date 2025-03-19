class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = ListNode(homepage)
        self.size=0

    def visit(self, url: str) -> None:
        new_node = ListNode(url)
        self.curr.next = new_node
        new_node.prev = self.curr
        self.curr = new_node
        self.size+=1

    def back(self, steps: int) -> str:
        if steps<0:
            return -1
        if self.curr:
            while(self.curr.prev is not None and steps>0):
                self.curr = self.curr.prev
                steps-=1
            return self.curr.val

    def forward(self, steps: int) -> str:
        if steps<0:
            return -1
        if self.curr:
            while(self.curr.next is not None and steps>0):
                self.curr = self.curr.next
                steps-=1
            return self.curr.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)