"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        if root is None:
            return root
        if root.left is not None :
            root.left.next = root.right
            
        if root.right is not None and root.next is not None:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        
        return root
        
        
        
        