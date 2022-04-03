class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def getData(self):
        return self.data
          
class BinaryTree:
    def __init__(self):
        self.root=None
    
    def insert(self,data):
        if self.root==None:
            self.root=Node(data)
            return
        elif self.root.left==None:
            self.root.left=Node(data)
            return
        elif self.root.right==None:
            self.root.right=Node(data)
            return
        else:
            listt = []
            listt.append(self.root)
            for k in listt:
                if k.left != None and k.right !=None:
                    listt.append(k.left)
                    listt.append(k.right)
            else:
                if k.left == None:
                    k.left = Node(data)
                    return
                else:
                    k.right = Node(data)
                    return  
            
    def searchNode(self, temp, val):  
        if(self.root == None):  
            print("Tree is empty")
        else:  
             if(temp.left != None):  
                self.searchNode(temp.left, val)
             if(temp.right != None):  
                self.searchNode(temp.right, val)        
        if(temp.data == val):  
            print("Present")
            return
        else:
            print("elemnt is not present")
            return
        
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
        if data == None:
            return 0
        Lheight = self.Height(data.left)
        Rheight = self.Height(data.right)
        
        if Lheight > Rheight:
            return Lheight + 1
        else:
            return Rheight + 1
        

    def User(self):
            print("""
                  a. Insert
                  b. Search
                  c. Pre-Order
                  d. In-Order 
                  e. Post-Order 
                  f. Height
                  g. End the program.""")
            while True: 
                A = input("Choose the Option::")
                if (A=="a"):
                    data = int(input("Enter the element to insert:: "))
                    tree.insert(data)
                if (A=="b"):
                    data = int(input("Enter the element to search:: "))
                    tree.searchNode(self.root,data)
                if (A=="c"):
                    print("Pre-Order::")
                    print(tree.Pre_Order(tree.root, ""))
                if (A=="d"):
                    print("In-Order::")
                    print(tree.In_Order(tree.root, ""))               
                if (A=="e"):
                    print("Post-Order::")
                    print(tree.Post_Order(tree.root, ""))
                if (A=="f"):
                    print("Height is:")
                    print(tree.Height(self.root))
                if (A=="g"):
                    print("Program Ended Succesfully")
                    break
        
tree  = BinaryTree()
tree.User()
               
   
     

        
    
    