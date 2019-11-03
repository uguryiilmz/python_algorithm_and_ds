class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def leafSimilar(self,root1):
        res=[]
        def searchTree(root):
            if(root):
                if (root.left):
                    searchTree(root.left)
                if (root.right):
                     searchTree(root.right)
                if root.right==None and root.left==None:
                    res.append(root)
                    return

        searchTree(root1)


        

tree=TreeNode(3)
tree.left=TreeNode(5)
tree.right=TreeNode(1)
tree.left.left=TreeNode(6)
tree.left.right=TreeNode(2)
tree.left.right.left=TreeNode(7)
tree.left.right.right=TreeNode(4)
tree.right.left=TreeNode(9)
tree.right.right=TreeNode(8)


sol=Solution()

print(sol.leafSimilar(tree))