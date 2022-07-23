#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-19 14:40:28
LastEditTime: 2022-03-19 14:41:14
Description: 
FilePath: 515.在每个树行中找最大值.py
"""
#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#

from collections import defaultdict
# @lc code=start
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        self.levelnodes = defaultdict(list)

        def dfs(node, level):
            if not node:
                return
            self.levelnodes[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)

        # print(self.levelnodes)
        return [max(item) for item in self.levelnodes.values()]


# @lc code=end
