# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:return root
        res=[]
        def fun(root):
            if root.left: fun(root.left)
            res.append(root.val)
            if root.right: fun(root.right)
        fun(root)
        return min(b-a for a,b in zip(res,res[1:]))
        '''
        if not root: return root
        def fun(node,low,high):
            if not node: return high-low
            left=fun(node.left,low,node.val)
            right=fun(node.right,node.val,high)
            return min(left,right)
        return fun(root,float('-inf'),float('inf'))
        '''
        '''
        q=[root]
        l=[]
        while len(q):
            l.append(q[0].val)
            node=q.pop(0)
            if node:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        mn=float('inf')
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                if abs(l[i]-l[j]) < mn: mn = abs(l[i]-l[j])
        return mn
        '''