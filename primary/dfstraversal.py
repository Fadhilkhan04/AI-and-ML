class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None 

def inorderTraversal(root):
    answer = []

    inorderTraversalUtil(root, answer)
    return answer

def inorderTraversalUtil(root, answer):

    if root is None:
        return

    inorderTraversalUtil(root.left, answer)
    answer.append(root.val)
    inorderTraversalUtil(root.right, answer)
    return

def preorderTraversal(root):
    answer = []

    preorderTraversalUtil(root, answer)
    return answer

def preorderTraversalUtil(root, answer):

    if root is None:
        return 

    answer.append(root.val)

    preorderTraversalUtil(root.left, answer)

    preorderTraversalUtil(root.right, answer)

    return
def postorderTraversal(root):
    answer = []

    postorderTraversalUtil(root, answer)
    return answer

def postorderTraversalUtil(root, answer):

    if root is None:
        return

    postorderTraversalUtil(root.left, answer)

    postorderTraversalUtil(root.right, answer)

    answer.append(root.val)

    return

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
print(inorderTraversal(root))
print("the preorder traversal is : ")
print(preorderTraversal(root))
print("the postorder traversal is : ")
print(postorderTraversal(root))