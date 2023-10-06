#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-03 22:41
FileName: LCP
Description:LCR 150. 彩灯装饰记录 II.py 
"""
from collections import deque
from typing import Optional, List

from common.TreeNode import TreeNode


class Solution:
    def decorateRecord(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        queue = deque([root])
        while queue:
            level, n = [], len(queue)
            for i in range(n):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(level)
        return levels


if __name__ == '__main__':
    print(Solution().decorateRecord(TreeNode.create("[8,17,21,18,null,null,6]")))
