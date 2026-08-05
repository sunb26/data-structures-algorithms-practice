# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0
        left = 0
        right = 0

        def traverse(root):
            if not root:
                return 0
            
            nonlocal maxDiameter
            leftHeight = traverse(root.left)
            rightHeight = traverse(root.right)
            
            d = leftHeight + rightHeight
            
            maxDiameter = max(maxDiameter, d)

            return 1 + max(leftHeight, rightHeight)

        traverse(root)
        return maxDiameter