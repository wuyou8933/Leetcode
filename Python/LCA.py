class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
            :type root: TreeNode
            :type p: TreeNode
            :type q: TreeNode
            :rtype: TreeNode
            """
        if root in [None,p,q]: return root
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        return root if left and right else right or left