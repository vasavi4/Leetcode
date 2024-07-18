class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans = 0
        def calculator(node):
            if not node:
                return 

            if node.val >= low and node.val<=high:
                self.ans += node.val 

            if node.val>=low:
                calculator(node.left)
            if node.val<=high:
                calculator(node.right) 

        calculator(root)

        return self.ans

            
