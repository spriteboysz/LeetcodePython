#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-28 23:42:13
LastEditTime: 2022-03-28 23:46:20
Description: 
FilePath: 637.二叉树的层平均值.py
"""
#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#

from collections import deque
# @lc code=start
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        level, queue = [], deque()
        queue.append(root)
        while queue:
            curlevel = []
            for _ in range(len(queue)):
                node = queue.popleft()
                curlevel.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level.append(sum(curlevel) / len(curlevel))
        return level


# @lc code=end
