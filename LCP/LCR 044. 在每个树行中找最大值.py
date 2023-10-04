#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-01 22:40
FileName: LCP
Description:LCR 044. 在每个树行中找最大值.py 
"""
from collections import deque
from typing import List

from common.TreeNode import TreeNode


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        levels = []
        if not root:
            return levels
        queue = deque([root])
        while queue:
            n, level = len(queue), []
            for i in range(n):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(max(level))
        return levels


if __name__ == '__main__':
    print(Solution().largestValues(TreeNode.create("[1,3,2,5,3,null,9]")))
