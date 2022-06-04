#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-31 23:58:13
LastEditTime: 2022-04-01 00:04:03
Description:
FilePath: 1609.奇偶树.py
"""
#
# @lc app=leetcode.cn id=1609 lang=python3
#
# [1609] 奇偶树
#

from collections import deque
# @lc code=start
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return

        level, queue = 0, deque([root])
        while queue:
            curlevel = []
            for _ in range(len(queue)):
                node = queue.popleft()
                curlevel.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level % 2:
                curlevel = curlevel[::-1]
                for item in curlevel:
                    if item % 2 == 1:
                        return False
            else:
                for item in curlevel:
                    if item % 2 == 0:
                        return False

            for i in range(len(curlevel) - 1):
                if curlevel[i + 1] - curlevel[i] <= 0:
                    return False
            level += 1
        return True



