# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def traverse(root, pVal, qVal):
            if not root:
                return None
            if root.val == pVal or root.val == qVal:
                return root
            elif root.val > pVal and root.val < qVal:
                return root
            elif root.val < pVal and root.val > qVal:
                return root
            elif root.val > pVal and root.val > qVal:
                return traverse(root.left, pVal, qVal)
            else:
                return traverse(root.right, pVal, qVal)
        
        return traverse(root, p.val, q.val)