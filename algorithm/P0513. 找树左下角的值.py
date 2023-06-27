#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-19 14:54:24
LastEditTime: 2022-03-19 14:56:53
Description: 
FilePath: 513.找树左下角的值.py
"""

from collections import deque
from typing import Optional

from common.TreeNode import TreeNode


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue, left = deque(), None
        queue.append(root)
        while queue:
            left = queue[0].val
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return left
