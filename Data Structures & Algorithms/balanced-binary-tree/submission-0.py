# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        balanced = True

        def traverse(root):
            if not root:
                return 0
            
            nonlocal balanced

            left = traverse(root.left) + 1
            right = traverse(root.right) + 1

            if abs(right - left) > 1:
                balanced = False
            
            return max(left, right)
        
        traverse(root)

        return balanced

