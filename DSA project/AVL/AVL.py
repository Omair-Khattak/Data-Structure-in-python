class Node:
    def __init__(self,d):
        self.data=d[0][1]
        self.fullData=d
        self.left=None
        self.right=None

    def get_data(self):   
        return self.data  

    def get_fullData(self):
        return self.fullData

class AVL_tree:
    def __init__(self):
        self.root=None

    def get_root(self):
        return self.root

    def insert(self,root,new_node):
        if self.root==None:
            self.root=new_node
            return
        if root == None:
            return new_node
        else:
            if root.data>=new_node.data:
                root.left = self.insert(root.left,new_node)    
            else:
                root.right = self.insert(root.right,new_node)
                
        balance=self.get_balance(root) 

        if balance>1 and new_node.data<root.left.data: 
            return self.right_rotate(root) 

        if balance<-1 and new_node.data>root.right.data: 
            return self.left_rotate(root) 

        if balance>1 and new_node.data>root.left.data: 
            root.left=self.left_rotate(root.left) 
            return  self.right_rotate(root) 

        if balance<-1 and new_node.data<root.right.data: 
            root.right=self.right_rotate(root.right) 
            return  self.left_rotate(root) 

        return root   

    def left_rotate(self,root): 
        data1=root.right 
        data2=data1.left 

        data1.left=root
        root.right=data2

        if root.data == self.root.data:
            self.root = data1
        return data1
  
    def right_rotate(self,root): 
        data1=root.left 
        data2=data1.right 
  
        data1.right=root 
        root.left=data2

        if root.data == self.root.data:
            self.root = data1

        return data1
  
  
    def get_balance(self, root): 
        return self.height_of_tree(root.left) - self.height_of_tree(root.right) 
  
    def search(self,root,value):
        if self.root==value:
            print(root.fullData)
            return
        while True:
            if root.left!=None or root.right!=None:
                if root.data<value:
                    if root.right.data==value:
                        print(root.right.fullData)
                        return
                    root=root.right

                else:
                    if root.left.data==value:
                        print(root.left.fullData)
                        return
                    root=root.left
            else:
                break
        print("not found")
        
    def height_of_tree(self,root):
        if self.root==None:
            print("Tree is empty")
        elif root == None:
            return 0
        else:
            left_height=0
            right_height=0
            if root.left!=None:
                left_height=self.height_of_tree(root.left)    
            if root.right!=None:
                right_height=self.height_of_tree(root.right)    
            if left_height>right_height:
                return left_height+1
            else:
                return right_height+1 
  

    def minimum_Node(self,current):
        while(current.left != None):
            current = current.left
        return current
          

f = open("Data.txt", "r")
data1 = f.read()
data1 = data1.split()
data2 = [[]for i in range(10,101)]
first=3
second=4
third=5
while first < len(data1):
    x = int(float(data1[second])*10)
    data2[x-10].append([data1[first],float(data1[second]), int(data1[third])])
    first += 3
    second += 3
    third += 3

tree = AVL_tree()
for i in data2:
    tree.insert(tree.get_root(),Node(i))

print("a. Movie Having MAXIMUM rating"
"\n""b. Movie Having SAME rating"
"\n""c. Movie Having MINIMUM rating"
"\n""d. Exit (stop the program)")


while True:
    choice=input("enter choice from a to d: ")
    if choice=="a":
        tree.search(tree.get_root(),10.0)
    
    elif choice=="b":
        num=float(input("Enter average rating to know number of movies having same ratings: "))
        tree.search(tree.get_root(),num)
   
    elif choice=="c":
        tree.search(tree.get_root(),1.0)
   
    elif choice=="d":
        print("program is stop")
        break
      
    else:
        print("invalid input")