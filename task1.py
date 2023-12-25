class Node:
 def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def height(node):
    if node is None:
        return 0
    else:
        left_height = height(node.left)
        right_height = height(node.right)
        return max(left_height, right_height) + 1

root = None
keys = [11, 55, 1, 4, 8, 112, 17, 23, -2, 34, 2]
for key in keys:
    root = insert(root, key)
print("Висота бінарного дерева:", height(root))
