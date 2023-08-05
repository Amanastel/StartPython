class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):
    if root is None:
        return None

    # Swap left and right children
    root.left, root.right = root.right, root.left

    # Invert the left and right subtrees
    invert_tree(root.left)
    invert_tree(root.right)

    return root


# Example usage
# Construct a binary tree
tree = TreeNode(4)
tree.left = TreeNode(2)
tree.right = TreeNode(7)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(3)
tree.right.left = TreeNode(6)
tree.right.right = TreeNode(9)

# Invert the binary tree
inverted_tree = invert_tree(tree)


# Helper function to print tree nodes (in-order traversal)
def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.val, end=" ")
        print_tree(root.right)


# Print the original and inverted trees
print("Original tree:")
print_tree(tree)
print("\nInverted tree:")
print_tree(inverted_tree)
