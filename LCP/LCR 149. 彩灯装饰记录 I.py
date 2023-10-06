#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-03 22:34
FileName: LCP
Description:LCR 149. 彩灯装饰记录 I.py 
"""
from collections import deque
from typing import Optional, List

from common.TreeNode import TreeNode


class Solution:
    def decorateRecord(self, root: Optional[TreeNode]) -> List[int]:
        levels = []
        if not root:
            return levels
        queue = deque([root])
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                levels.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return levels


if __name__ == '__main__':
    print(Solution().decorateRecord(TreeNode.create("[8,17,21,18,null,null,6]")))
