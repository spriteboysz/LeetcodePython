#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-29 22:49:42
LastEditTime: 2022-03-29 22:55:59
Description: 
FilePath: 112.路径总和.py
"""
#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        queue = deque()
        queue.append((root, root.val))
        while queue:
            node, pathsum = queue.popleft()
            if not node.left and not node.right:
                if pathsum == targetSum:
                    return True
            if node.left:
                queue.append((node.left, pathsum + node.left.val))
            if node.right:
                queue.append((node.right, pathsum + node.right.val))
        return False

# @lc code=end
