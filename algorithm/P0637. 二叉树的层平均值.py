#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-28 23:42:13
LastEditTime: 2022-03-28 23:46:20
Description: 
FilePath: 637.二叉树的层平均值.py
"""

from collections import deque
from typing import List, Optional

from common.TreeNode import TreeNode


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        levels, queue = [], deque()
        queue.append(root)
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(sum(level) / len(level))
        return levels


if __name__ == '__main__':
    solution = Solution()
    print(solution.averageOfLevels(TreeNode.create("[3,9,20,null,null,15,7]")))
