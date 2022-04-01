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

# @lc code=start
# Definition for a binary tree node.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return

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
            if len(level) % 2:
                curlevel = curlevel[::-1]
            level.append(curlevel)
        
        for i, curlevel in enumerate(level):
            if i % 2 == 0:
                pass



# @lc code=end
