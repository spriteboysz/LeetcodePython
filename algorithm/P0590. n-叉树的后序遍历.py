#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N 叉树的后序遍历
#

# @lc code=start
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: "Node") -> List[int]:
        value = []

        def dfs(node):
            if not node:
                return
            for child in node.children:
                dfs(child)
            value.append(node.val)

        dfs(root)
        return value

# @lc code=end
