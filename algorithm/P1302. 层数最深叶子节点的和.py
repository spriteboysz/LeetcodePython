#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-19 14:04:53
LastEditTime: 2022-03-19 14:05:37
Description: 
FilePath: 1302.层数最深叶子节点的和.py
"""
from collections import deque
from typing import Optional

from common.TreeNode import TreeNode


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        levels = 0
        if not root:
            return levels
        queue = deque()
        queue.append(root)
        while len(queue) != 0:
            levels = 0
            size = len(queue)
            for i in range(0, size):
                node = queue.popleft()
                levels += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return levels


if __name__ == '__main__':
    solution = Solution()
    print(solution.deepestLeavesSum(TreeNode.create("[1,2,3,4,5,null,6,7,null,null,null,null,8]")))
