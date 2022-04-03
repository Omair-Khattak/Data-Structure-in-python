class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def getData(self):
        return self.data
          
class BinarySearchTree:
    def __init__(self):
        self.root=None
    
    def insert(self,data):
        if self.root==None:
            self.root=Node(data)
        else:
            self.insertATboth(data,self.root)
    
    def deleteNode(self, root, data):
        if not root:
            return root
        elif data < root.data:
            root.left = self.deleteNode(root.left, data)
        elif data > root.data:
            root.right = self.deleteNode(root.right, data)
        else:
            #condition 1: if we have to delete only leaf which means it has no children
            if not root.left and not root.right:
                root = None
            #condition 2: if the element we want to delete has only one child
            elif not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else:
            #condition 3: if the element we want to delete has 2 children
                temp = self.findmin(root.right)
                root.data = temp.data
                root.right = self.deleteNode(root.right, temp.data)
        return root
    #to find minimum while deleting a Node
    def findmin(self, root):
        current = root
        while current.left:
            current = current.left
        return current
            
    def insertATboth(self,data,Cnode):
          if data < Cnode.data:
            if Cnode.left is None:              
                Cnode.left = Node(data)
            else:
                self.insertATboth(data, Cnode.left)     #For Insert at Left
          else:
              if Cnode.right == None:
                  Cnode.right = Node(data)
              else:
                  self.insertATboth(data, Cnode.right)  #For Insert at right
            
    def searchNode(self,root, key):  
        if root is None: 
            return root 
        if root.data == key:
            print("Found")
            return
        elif root.data < key: 
            found = self.searchNode(root.right,key) 
            if found:
                print("found")
                return
            else:
                print("Not found")
        else:
            found = self.searchNode(root.left,key)
            if found:
                print("found")
                return
            else:
                print("Not found")

    


        
    def Pre_Order(self,strt,trvrsal):
        if strt:
                trvrsal += str(strt.data) + "=>"
                trvrsal = self.Pre_Order(strt.left, trvrsal)
                trvrsal = self.Pre_Order(strt.right, trvrsal)
        return trvrsal
    def In_Order(self,strt,trvrsal):
        if strt:
                trvrsal = self.In_Order(strt.left, trvrsal)
                trvrsal += str(strt.data) + "=>"
                trvrsal = self.In_Order(strt.right, trvrsal)
        return trvrsal
    def Post_Order(self,strt,trvrsal):
        if strt:
                trvrsal = self.Post_Order(strt.left, trvrsal)
                trvrsal = self.Post_Order(strt.right, trvrsal)
                trvrsal += str(strt.data) + "=>"
        return trvrsal
    
    def Height(self, data):
        if(self.root == None):  
            print("No root is found in tree")
            return 0
        else:  
            leftH = 0
            rightH = 0
            if(data.left != None):  
                leftH = self.Height(data.left);  
            if(data.right != None):  
                rightH = self.Height(data.right);  
            if (leftH > rightH):
                maxx = leftH
            else:
                maxx = rightH
            return (maxx + 1) 
        

    def User(self):
            print("""
                  a. Insert a Node in BST
                  b. Delete a Node from BST
                  c. Search
                  d. Pre-Order
                  e. In-Order 
                  f. Post-Order 
                  g. Height
                  h. End the program.""")
            while True: 
                A = input("Choose the Option::")
                if (A=="a"):
                    data = int(input("Enter the element to insert:: "))
                    tree.insert(data)
                if (A=="b"):
                    data = int(input("Enter the element to delete:: "))
                    tree.deleteNode(self.root, data)
                if (A=="c"):
                    data = int(input("Enter the element to search:: "))
                    tree.searchNode(self.root,data)
                if (A=="d"):
                    print("Pre-Order::")
                    print(tree.Pre_Order(tree.root, ""))
                if (A=="e"):
                    print("In-Order::")
                    print(tree.In_Order(tree.root, ""))               
                if (A=="f"):
                    print("Post-Order::")
                    print(tree.Post_Order(tree.root, ""))
                if (A=="g"):
                    print("Height is:")
                    print(tree.Height(self.root))
                if (A=="h"):
                    print("Program Ended Succesfully")
                    break
                
        
tree  = BinarySearchTree()
tree.User()
               
   
     

        
    
    