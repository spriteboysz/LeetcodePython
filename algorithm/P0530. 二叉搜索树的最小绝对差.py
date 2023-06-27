#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-28 23:34:44
LastEditTime: 2022-03-28 23:40:06
Description: 
FilePath: 530.二叉搜索树的最小绝对差.py
"""

from math import inf

from common.TreeNode import TreeNode


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        values = []
        dfs(root)

        minimum = inf
        for i in range(1, len(values)):
            minimum = min(values[i] - values[i - 1], minimum)
        return minimum


if __name__ == '__main__':
    solution = Solution()
    print(solution.getMinimumDifference(TreeNode.create("[4,2,6,1,3]")))
