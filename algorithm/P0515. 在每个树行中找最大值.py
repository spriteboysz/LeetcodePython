#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-19 14:40:28
LastEditTime: 2022-03-19 14:41:14
Description: 
FilePath: 515.在每个树行中找最大值.py
"""

from collections import deque
from math import inf
from typing import List, Optional

from common.TreeNode import TreeNode


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue, ans = deque([root]), []
        while queue:
            cur = -inf
            for _ in range(len(queue)):
                node = queue.popleft()
                cur = max(cur, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(cur)
        return ans
