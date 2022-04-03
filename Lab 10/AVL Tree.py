class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if not root:
            return Node(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))

        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if data < root.left.data:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if data > root.right.data:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    def delete(self, root, data):

        # Find the node to be deleted and remove it
        if not root:
            return root
        elif data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.data:
            root.right = self.delete(root.right, data)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.findmin(root.right)
            root.data = temp.data
            root.right = self.delete(root.right,
                                          temp.data)
        if root is None:
            return root
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def findmin(self, root):
        if root is None or root.left is None:
            return root
        return self.findmin(root.left)

    def searchNode(self, root, data):
        if root is None:
            return root
        if root.data == data:
            print("Found")
            return
        elif root.data < data:
            found = self.searchNode(root.right, data)
            if found:
                print("found")
                return
            else:
                print("Not found")
        else:
            found = self.searchNode(root.left, data)
            if found:
                print("found")
                return
            else:
                print("Not found")

    def preOrder(self, root):
        if not root:
            return
        print(root.data)
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        print(root.data)
        self.inOrder(root.right)

    def postOrder(self, root):
        if not root:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data)
    def User(self):
        while True:
            print("""
                              a. Insert a Node in BST
                              b. Delete a Node from BST
                              c. Search
                              d. Pre-Order
                              e. In-Order 
                              f. Post-Order 
                              g. Height
                              h. End the program.""")
            A = input("Choose the Option::")
            if (A == "a"):
                nums = []
                n = int(input("How many elements do you want to insert:"))
                for i in range(0, n):
                    data = int(input("Enter the element to insert:: "))
                    nums.append(data)
                root = None
                for num in nums:
                    root = myTree.insert(root, num)
            if (A == "b"):
                data = int(input("Enter the element to delete:: "))
                myTree.delete(root, data)
            if (A == "c"):
                data = int(input("Enter the element to search:: "))
                myTree.searchNode(root, data)
            if (A == "d"):
                print("Pre-Order::")
                myTree.preOrder(root)
            if (A == "e"):
                print("In-Order::")
                myTree.inOrder(root)
            if (A == "f"):
                print("Post-Order::")
                myTree.postOrder(root)
            if (A == "h"):
                print("Program Ended Succesfully")
                break



myTree = AVLTree()
myTree.User()