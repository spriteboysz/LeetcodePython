#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-29 23:12:01
LastEditTime: 2022-03-29 23:17:14
Description: 
FilePath: 653.两数之和-iv-输入-bst.py
"""

from typing import Optional

from common.TreeNode import TreeNode


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        values = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        dfs(root)
        for i in range(len(values) - 1):
            if k - values[i] in values[i + 1:]:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.findTarget(TreeNode.create("[5,3,6,2,4,null,7]"), 9))
