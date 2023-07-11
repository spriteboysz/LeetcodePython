#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-25 00:01
FileName: algorithm/P2415. 反转二叉树的奇数层.py
Description: 
"""
from collections import deque
from typing import Optional

from common.TreeNode import TreeNode


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        depth, queue = 0, deque()
        queue.append(root)
        while len(queue) > 0:
            size, level, value = len(queue), [], []
            for i in range(size):
                node = queue.popleft()
                level.append(node)
                value.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if depth % 2 == 1:
                value.reverse()
                for i, node in enumerate(level):
                    node.val = value[i]
            depth += 1
        return root


if __name__ == '__main__':
    root = TreeNode.create("[2,3,5,8,13,21,34]")
    solution = Solution().reverseOddLevels(root)
    print(solution)
