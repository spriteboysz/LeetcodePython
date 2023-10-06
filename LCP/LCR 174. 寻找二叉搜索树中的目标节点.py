#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-03 23:10
FileName: LCP
Description:LCR 174. 寻找二叉搜索树中的目标节点.py 
"""
from typing import Optional

from common.TreeNode import TreeNode


class Solution:
    values = []

    def dfs(self, root: Optional[TreeNode]):
        if not root:
            return
        self.dfs(root.left)
        self.values.append(root.val)
        self.dfs(root.right)

    def findTargetNode(self, root: Optional[TreeNode], cnt: int) -> int:
        self.dfs(root)
        return self.values[-cnt]


if __name__ == '__main__':
    print(Solution().findTargetNode(TreeNode.create("[7, 3, 9, 1, 5]"), 2))
