#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-29 23:31:17
LastEditTime: 2022-03-29 23:35:53
Description: 
FilePath: 988.从叶结点开始的最小字符串.py
"""
#
# @lc app=leetcode.cn id=988 lang=python3
#
# [988] 从叶结点开始的最小字符串
#

# @lc code=start
from typing import Optional
from collections import deque
from string import ascii_lowercase

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if not root:
            return
        paths, queue = [], deque()
        queue.append((root, ascii_lowercase[root.val]))
        while queue:
            node, path = queue.popleft()
            if not node.left and not node.right:
                paths.append(path[::-1])
            if node.left:
                queue.append((node.left, path + ascii_lowercase[node.left.val]))
            if node.right:
                queue.append((node.right, path + ascii_lowercase[node.right.val]))
        return sorted(paths)[0]


# @lc code=end
