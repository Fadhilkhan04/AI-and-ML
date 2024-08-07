class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
 
# A function to do inorder tree traversal
def printInorder(root):
 
    if root:
 
        # First recur on left child
        printInorder(root.left)
 
        # then print the data of node
        print(root.val) 
 
        # now recur on right child
        printInorder(root.right)

def printPreorder(root):
 
    if root:
 
        # First print the data of node
        print(root.val)
 
        # Then recur on left child
        printPreorder(root.left)
 
        # Finally recur on right child
        printPreorder(root.right)

def printPostorder(root):
 
    if root:
 
        # First recur on left child
        printPostorder(root.left)
 
        # the recur on right child
        printPostorder(root.right)
 
        # now print the data of node
        print(root.val)
 
root = TreeNode('F')
root.left = TreeNode('B')
root.right = TreeNode('G')
root.left.left = TreeNode('A')
root.left.right = TreeNode('D')
root.left.right.left = TreeNode('C')
root.left.right.right = TreeNode('E')
root.right.right = TreeNode('I')
root.right.right.left = TreeNode('H')

print("the inorder traversal is : ")
print(printInorder(root))
print("the preorder traversal is : ")
print(printPreorder(root))
print("the postorder traversal is : ")
print(printPostorder(root))