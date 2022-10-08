#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-29 23:42:46
LastEditTime: 2022-03-29 23:48:21
Description: 
FilePath: 559.n-叉树的最大深度.py
"""
#
# @lc app=leetcode.cn id=559 lang=python3
#
# [559] N 叉树的最大深度
#

# @lc code=start
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: "Node") -> int:
        if not root:
            return 0
        level, queue = 0, deque()
        queue.append(root)
        while queue:
            # curlevel = []
            for _ in range(len(queue)):
                node = queue.popleft()
                # curlevel.append(node.val)
                for child in filter(bool, node.children):
                    queue.append(child)
            level += 1
        return level


# @lc code=end
