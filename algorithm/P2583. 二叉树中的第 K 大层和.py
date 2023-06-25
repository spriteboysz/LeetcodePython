#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-06-25 22:29
FileName: algorithm/P2583. 二叉树中的第 K 大层和.py
Description: 
"""
from collections import deque
from typing import Optional

from common.TreeNode import TreeNode


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        levels = []
        queue = deque()
        queue.append(root)
        while len(queue) != 0:
            level, size = 0, len(queue)
            for i in range(size):
                node = queue.popleft()
                level += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(level)
        if len(levels) < k:
            return -1
        levels.sort(reverse=True)
        return levels[k - 1]


if __name__ == '__main__':
    print(Solution().kthLargestLevelSum(TreeNode.create("[5,8,9,2,1,3,7,4,6]"), 2))
