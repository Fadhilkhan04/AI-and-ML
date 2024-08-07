

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None



def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printCurrentLevel(root, i)



def printCurrentLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.right, level-1)



def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1


if __name__ == '__main__':
    root = Node('F')
    root.left = Node('B')
    root.right = Node('G')
    root.left.left = Node('A')
    root.left.right = Node('D')
    root.left.right.left = Node('C')
    root.left.right.right = Node('E')
    root.right.right = Node('I')
    root.right.right.left = Node('H')

    printLevelOrder(root)