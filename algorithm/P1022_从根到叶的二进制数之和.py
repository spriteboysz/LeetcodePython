#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-29 23:56:27
LastEditTime: 2022-03-30 00:00:16
Description: 
FilePath: 1022.从根到叶的二进制数之和.py
"""
#
# @lc app=leetcode.cn id=1022 lang=python3
#
# [1022] 从根到叶的二进制数之和
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
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        paths, queue = [], deque()
        queue.append((root, str(root.val)))
        while queue:
            node, path = queue.popleft()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                queue.append((node.left, path + str(node.left.val)))
            if node.right:
                queue.append((node.right, path + str(node.right.val)))
        print(paths)
        return sum(map(lambda el: int(el, 2), paths))


# @lc code=end
