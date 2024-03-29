# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        
        # initializing a tree node to store the merged tree 
        t = TreeNode(root1.val+root2.val)
        
        t.left = self.mergeTrees(root1.left, root2.left)
        t.right = self.mergeTrees(root1.right , root2.right)
    
        return t
        