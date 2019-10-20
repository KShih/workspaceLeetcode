def sumOfLeaves(self, root: TreeNode) -> int:
    def add_leaves(root, val):
        if not root.left and not root.right:
            return root.val
        if root.left:
            val += add_leaves(root.left, val)
            print(val)
        if root.right:
            val += add_leaves(root.right, val)
            print(val)

        return val

    if (not root or (not root.left)):   return 0
    val = 0
    return add_leaves(root, val)
