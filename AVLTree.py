from treeEl import El
from stack import Stack


class AVLTree(object):

    def insert(self, root, key):

        if root is None:
            return El(key)

        if key == root.value:
            raise ValueError("Элемет с введённым ключом уже существует")

        if key < root.value:
            root.left = self.insert(root.left, key)

        if key > root.value:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balanceIndex = self.getBalance(root)

        if balanceIndex > 1 and key < root.left.value:
            return self.rightRotate(root)

        if balanceIndex > 1 and key > root.left.value:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balanceIndex < -1 and key > root.right.value:
            return self.leftRotate(root)

        if balanceIndex < -1 and key < root.right.value:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, q):
        p = q.right
        q.right = p.left
        p.left = q

        q.height = 1 + max(self.getHeight(q.left), self.getHeight(q.right))
        p.height = 1 + max(self.getHeight(p.left), self.getHeight(p.right))

        return p

    def rightRotate(self, p):
        q = p.left
        p.left = q.right
        q.right = p

        p.height = 1 + max(self.getHeight(p.left), self.getHeight(p.right))
        q.height = 1 + max(self.getHeight(q.left), self.getHeight(q.right))

        return q

    @staticmethod
    def getHeight(root):
        if root is None:
            return 0

        return root.height

    def getBalance(self, root):
        if root is None:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    @staticmethod
    def search(root, value):
        treeEl = AVLTree.rootLeftRight(root)
        if value in treeEl:
            return True
        else:
            return False

    @staticmethod
    def LeftRightRoot(root):  # ЛПК
        res = []
        stack = []

        while True:
            while root is not None:
                stack.append(root)
                stack.append(root)
                root = root.left

            if len(stack) == 0:
                return res

            root = stack.pop()

            if len(stack) > 0 and stack[-1] == root:
                root = root.right
            else:
                res.append(root.value)
                root = None

    @staticmethod
    def rootLeftRight(root):  # КЛП
        res = []
        stack = []

        if root is None:
            return

        stack.append(root)

        while len(stack) > 0:
            node = stack.pop()
            res.append(node.value)

            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return res

    @staticmethod
    def leftRootRight(root):  # ЛКП
        r = root
        res = []
        stack = []

        while True:
            if r is not None:
                stack.append(r)
                r = r.left

            elif stack:
                r = stack.pop()
                res.append(r.value)
                r = r.right

            else:
                break

        return res

    @staticmethod
    def sort(sequence):
        Tree = AVLTree()
        a = None
        for i in sequence:
            a = Tree.insert(a, i)
        return AVLTree.leftRootRight(a)

    def printTree(self, root, level=0):
        if root is not None:
            self.printTree(root.left, level + 1)
            print(' ' * 8 * level + '\t->', root.value)
            self.printTree(root.right, level + 1)
