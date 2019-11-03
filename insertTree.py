class TreeNode :
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None




arr=[-10,-3,0,5,9]


tree=TreeNode(arr[2])

class Solution:
    def insert(self,root,val):
        if val<root.val:
            if root.left:
                self.insert(root.left,val)
            else:
                root.left=TreeNode(val)
        else:
            if root.right:
                self.insert(root.right,val)
            else:
                root.right=TreeNode(val)

    def sortedArrayToBST(self, num):
        if not num:
            return None

        mid = len(num) // 2

        root = TreeNode(num[mid])
''        root.left = self.sortedArrayToBST(num[:mid])
        root.right = self.sortedArrayToBST(num[mid+1:])

        return root

sol=Solution()
sol.sortedArrayToBST(arr)