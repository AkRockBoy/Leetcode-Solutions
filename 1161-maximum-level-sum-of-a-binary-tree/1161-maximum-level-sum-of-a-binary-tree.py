class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=[root]
        ans=[]
        while len(q) > 0:
            length=len(q)
            res=[]
            for i in range(length):
                node=q.pop(0)
                res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(sum(res))
        mx=max(ans)
        return 1+ans.index(mx)