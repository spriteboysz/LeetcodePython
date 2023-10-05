#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-02 16:56
FileName: LCP
Description:LCR 054. 把二叉搜索树转换为累加树.py 
"""
from common.TreeNode import TreeNode


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root:
                return
            nonlocal acc
            dfs(root.right)
            acc += root.val
            root.val = acc
            dfs(root.left)

        acc = 0
        dfs(root)
        return root


if __name__ == '__main__':
    print(Solution().convertBST(TreeNode.create("[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]")))
