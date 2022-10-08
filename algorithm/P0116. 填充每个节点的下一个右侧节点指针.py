#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-31 22:45:28
LastEditTime: 2022-03-31 22:50:29
Description: 
FilePath: 116.填充每个节点的下一个右侧节点指针.py
"""
#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

from collections import deque
# @lc code=start
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return

        queue = deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i < size - 1:
                    node.next = queue[0]

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root


# @lc code=end
