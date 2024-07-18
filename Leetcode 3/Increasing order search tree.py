class Solution(object):
    def increasingBST(self, root):
        arr = []
	def dfs(node):
		if not(node):
			return 
		dfs(node.left)
		arr.append(node.val)
		dfs(node.right)

	dfs(root)
	root = curr = TreeNode(arr[0])
	for i in arr[1:]:
		curr.right = TreeNode(i)
		curr = curr.right
	return root
