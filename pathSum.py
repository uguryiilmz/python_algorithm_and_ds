class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
    
class Solution(object):
    def hashPathSum(self, root, sum):
        if root==None:
            return False
        
        if root.left==None and root.right==None and sum-root.val==0:
            return True
        
        return self.hashPathSum(root.left,sum-root.val) or self.hashPathSum(root.right,sum-root.val)


tree=TreeNode(5)
tree.left=TreeNode(4)
tree.left.left=TreeNode(11)
tree.left.left.left=TreeNode(7)
tree.left.left.right=TreeNode(2)

tree.right=TreeNode(8)
tree.right.left=TreeNode(13)
tree.right.right=TreeNode(4)
tree.right.right.right=TreeNode(1)


sol=Solution()
sol.hashPathSum(tree,22)