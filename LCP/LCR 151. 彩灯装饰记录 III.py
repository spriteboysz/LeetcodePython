#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-03 22:45
FileName: LCP
Description:LCR 151. 彩灯装饰记录 III.py 
"""
from collections import deque
from typing import Optional, List

from common.TreeNode import TreeNode


class Solution:
    def decorateRecord(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        queue, depth = deque([root]), 1
        while queue:
            level, n = [], len(queue)
            for i in range(n):
                node = queue.popleft()
                if depth % 2 == 1:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
            levels.append(level)
        return levels


if __name__ == '__main__':
    print(Solution().decorateRecord(TreeNode.create("[8,17,21,18,null,null,6]")))
