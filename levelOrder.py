import collections

# Definition for a binary tree node.
class TreeNode :
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None



class Solution :
    def levelOrder(self,root):
        q, result= collections.deque() ,[]
        if root:
            q.append(root)
        while len(q):
            level=[]
            for _ in range(len(q)):
                x=q.popleft()
                level.append(x.val)

                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
            
            result.append(level)
        return result
    
    def dfsLevelOrder(self,root):
        result=[]
        self.isHelper(root,0,result)
        return result

    def isHelper(self,root,level,result):
        if root==None:
            return
        if len(result)<=level:
            result.append([])
        result[level].append(root.val)
        self.isHelper(root.left,level+1,result)
        self.isHelper(root.right,level+1,result)

tree=TreeNode(3)
tree.left=TreeNode(9)
tree.right=TreeNode(20)
tree.right.left=TreeNode(15)
tree.right.right=TreeNode(7)

sol=Solution()

print(sol.dfsLevelOrder(tree))