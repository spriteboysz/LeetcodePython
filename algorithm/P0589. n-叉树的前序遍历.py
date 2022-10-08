#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-07 23:50:50
LastEditTime: 2022-03-07 23:53:12
Description: 
FilePath: 589.n-叉树的前序遍历.py
"""
#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N 叉树的前序遍历
#

# @lc code=start
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: "Node") -> List[int]:
        value = []
        def dfs(node):
            if node is None:
                return
            value.append(node.val)
            for child in node.children:
                dfs(child)

        dfs(root)
        return value


# @lc code=end
