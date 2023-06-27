#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-27 22:36:05
LastEditTime: 2022-03-27 22:38:55
Description: 
FilePath: 671.二叉树中第二小的节点.py
"""
from common.TreeNode import TreeNode


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return
            values.add(node.val)
            dfs(node.left)
            dfs(node.right)

        values = set()
        dfs(root)
        if len(values) == 1:
            return -1
        else:
            return sorted(list(values))[1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.findSecondMinimumValue(TreeNode.create("[2,2,5,null,null,5,7]")))
