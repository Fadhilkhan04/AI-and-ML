class TreeNode:
  def __init__(self,key):
    self.left = None
    self.right = None
    self.val = key

def preOrder(root):

  if root:
    print(root.val)
    preOrder(root.left)
    preOrder(root.right)

def inOrder(root):
  
  if root:
    inOrder(root.left)
    print(root.val)
    inOrder(root.right)

def postOrder(root):

  if root:
    postOrder(root.left)
    postOrder(root.right)
    print(root.val)

root = TreeNode('1')
root.left = TreeNode('2')
root.left.left = TreeNode('4')
root.left.right = TreeNode('5')
root.right = TreeNode('3')

print("Preorder Traversal :")
preOrder(root)
print("Inorder Traversal :")
inOrder(root)
print("Postorder Traversal :")
postOrder(root)