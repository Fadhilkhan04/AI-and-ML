class Node:
  def __init__(self,val):
    self.left = None
    self.right = None
    self.val = val

def printLevelOrder(root):

  if root:
    queue = []
    queue.append(root)

    while queue:
      m = queue.pop(0)
      print(m.val ,end=" ")

      if m.left:
        queue.append(m.left)
      if m.right:
        queue.append(m.right)

root = Node('1')
root.left = Node('2')
root.left.left = Node('4')
root.left.right = Node('5')
root.right = Node('3')

printLevelOrder(root)