from AVLTree import AVLTree

Tree = AVLTree()
root = None

root = Tree.insert(root, 100)
root = Tree.insert(root, 2)
root = Tree.insert(root, 3)
root = Tree.insert(root, 4)
root = Tree.insert(root, 5)
root = Tree.insert(root, 6)
root = Tree.insert(root, 10)
root = Tree.insert(root, 200)
root = Tree.insert(root, 33)
root = Tree.insert(root, 42)
root = Tree.insert(root, 51)
root = Tree.insert(root, 666)

Tree.printTree(root)

print(Tree.getHeight(root))
