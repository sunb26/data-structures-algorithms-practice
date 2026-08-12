# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodeCounter = 0

        def traverse(root, maxVal):
            if not root:
                return

            nonlocal goodNodeCounter
            
            if root.val >= maxVal:
                goodNodeCounter += 1
                maxVal = root.val
            
            traverse(root.left, maxVal)
            traverse(root.right, maxVal)

        traverse(root, -101) # lowest node val is -100
        return goodNodeCounter




