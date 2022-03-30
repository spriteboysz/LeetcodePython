#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-30 23:57:33
LastEditTime: 2022-03-31 00:01:13
Description: 
FilePath: 429.n-叉树的层序遍历.py
"""
#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N 叉树的层序遍历
#

# @lc code=start
from typing import List
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        if not root:
            return

        level, queue = [], deque()
        queue.append(root)
        while queue:
            curlevel = []
            for _ in range(len(queue)):
                node = queue.popleft()
                curlevel.append(node.val)
                for child in node.children:
                    queue.append(child)
            level.append(curlevel)
        return level


# @lc code=end
