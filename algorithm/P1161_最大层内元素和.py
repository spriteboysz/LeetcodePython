#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-03 21:32:44
LastEditTime: 2022-04-03 21:36:26
Description: 
FilePath: 1161.最大层内元素和.py
"""
#
# @lc app=leetcode.cn id=1161 lang=python3
#
# [1161] 最大层内元素和
#

from collections import deque
# @lc code=start
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        level, queue = [], deque([root])
        while queue:
            curlevel = []
            for _ in range(len(queue)):
                node = queue.popleft()
                curlevel.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level.append(sum(curlevel))
        # print(level)
        return level.index(max(level)) + 1


# @lc code=end
