# BFS广度优先算法，第一次找到的就是最小深度
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        que = collections.deque()
        que.append([root, 1])
        while que:
            node, depth = que.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                que.append([node.left, depth+1])
            if node.right:
                que.append([node.right, depth+1])
