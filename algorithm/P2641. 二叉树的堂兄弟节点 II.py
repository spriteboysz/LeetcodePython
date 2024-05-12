#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-10 23:03
FileName: algorithm
Description:P2641. 二叉树的堂兄弟节点 II.py 
"""
from typing import Optional

from common.TreeNode import TreeNode


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root.val = 0
        queue = [root]
        while queue:
            nodes = queue
            queue = []
            next_level_sum = 0
            for node in nodes:
                if node.left:
                    queue.append(node.left)
                    next_level_sum += node.left.val
                if node.right:
                    queue.append(node.right)
                    next_level_sum += node.right.val

            for node in nodes:
                children_sum = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)
                if node.left:
                    node.left.val = next_level_sum - children_sum
                if node.right:
                    node.right.val = next_level_sum - children_sum
        return root


if __name__ == '__main__':
    root = TreeNode.create("[5,4,9,1,10,null,7]")
    print(Solution().replaceValueInTree(root))
