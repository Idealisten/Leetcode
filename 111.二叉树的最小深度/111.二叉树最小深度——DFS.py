# 递归结束条件
# 叶子节点的定义是左孩子和右孩子都为 null 时叫做叶子节点
# 当 root 节点左右孩子都为空时，返回 1
# 当 root 节点左右孩子有一个为空时，返回不为空的孩子节点的深度
# 当 root 节点左右孩子都不为空时，返回左右孩子较小深度的节点值

class Solution:
    def minDepth(self, root) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if not root.left or not root.right:
            return left+right+1
        return min(left, right)+1
