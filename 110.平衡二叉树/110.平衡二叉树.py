# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root):
            if not root:    # 如果当前节点是null返回高度0
                return 0
            return max(height(root.left), height(root.right)) + 1
        if not root:
            return True
        return abs(
            height(
                root.left) -
            height(
                root.right)) <= 1 and self.isBalanced(
            root.left) and self.isBalanced(
                    root.right)
