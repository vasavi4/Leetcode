class Solution(object):
    def deepestLeavesSum(self, root):
        if not root: return 0
        h=[0]
        def dfs(root,depth):
            h[0]=max(h[0],depth)
            if root.left: dfs(root.left,depth+1)
            if root.right: dfs(root.right,depth+1)
        dfs(root,0)
        ans=[0]
        def find(root,depth):
            if depth==h[0]:
                ans[0]+=root.val
            if root.left: find(root.left,depth+1)
            if root.right: find(root.right,depth+1)
        find(root,0)
        return ans[0]
