class Data:
    def __init__(self,dataValue):
        self.value=dataValue
    def printData(self):
        print(self.value)
class Node:
    maxNumberofChildren=4       #  maximum number of children of a node 
                                #  It is also called order of the tree.
    def __init__(self):
        self.numberOfItems=0    #at the time of initialization, a node has 
                                #0 items.
        self.items=[]           #list to store values of a node
        self.children=[]        #list to store children of a node
        self.parent=None        #parent of a node
        
        #   Initializing children of a node to None
        for i in range(self.maxNumberofChildren):
            self.children.append(None)
            
        #   Initializing values of a node to None
        #   as number of values in a node is one less than the number of
        #   children of a node therefore j runs 1 iteration less.
        for j in range(self.maxNumberofChildren-1):
            self.items.append(None)
    
    #function to get parent of a Node
    def getParent(self):
        return self.parent
    
    #function to get a children (of a node) at given index
    def getChild(self, index):
        return self.children[index]
    
    #function to get value at given index of a node
    def getItemValue(self, index):
        return self.items[index]
    
    #function to get number of values present in a node
    def getNumberofValues(self):
        return self.numberOfItems
    
    #function to check whether a node is full or not? Means whether
    # it contains 4 keys or not
    def isFull(self):
        if self.numberOfItems==4:
            return True
        return False
    
    #Function to check whether given node is a leaf node or internal node
    def isLeaf(self):
        return not self.children[0]
    
    def findValue(self,valuetoBeFound):
        for i in range(self.maxNumberofChildren-1):
            if self.items[i]!=None:
                if self.items[i].value==valuetoBeFound:
                    return i       #index of value in the Node
        return -1
                
    
    #function to connect a child Node to its parent Node
    def connectChild (self, child, childNumber):
        self.children[childNumber]=child
        child.parent=self
    
    #function to display values of a Node
    def displayNode(self):
        for i in range(self.numberOfItems):
            self.items[i].printData()
            print("/")  # to display a slash beween values of a node
    
    #Function to remove largest value from the Node
    def removeLastValue(self):
        temp=self.items[self.numberOfItems-1]
        self.items[self.numberOfItems-1]=None
        self.numberOfItems-=1
        return temp
    
    #function to remove given children from the parent Node
    def removeChild(self, childNumber):
        tempChild=self.children[childNumber]
        self.children[childNumber]=None
        return tempChild
    
        
    def insertValue (self,newData):
        #newData is an object of the class Data created at the start
        
        self.numberOfItems+=1
        newValue=newData.value
        for i in reversed(range(self.maxNumberofChildren-1)):
            if self.items[i]==None:
                pass
            else:
                val=self.items[i].value
                if newValue < val:
                    self.items[i+1]=self.items[i]
                else:
                    self.items[i+1]=newData
                    return i+1
        self.items[0]=newData
        return 0
# The End of class Node
        
# Start of the class 2-3-4 Tree
        
class TwoThreeFourTree:
    
    #Constructor Function to initialize root of the tree.
    def __init__(self):
        self.root=Node()
    
    #Purpose of this function is to display all the values present in the tree.
    def displayTree(self):
        self.displayHelp(self.root, 0, 0)
        
    def displayHelp(self,node, level, child):
        print("level=",level, "Child=", child)
        node.displayNode()
        
        numberOfItems = node.getNumberofValues()
        for i in range(numberOfItems+1):
            nodeNext = node.getChild(i)
            if nodeNext:
                self.displayHelp(nodeNext, level+1, i)
            else:
                return
            
    def find(self,value):
        CurNode = self.root	
        while True:
            childNumber=CurNode.findValue(value)
            if childNumber != -1:
                return childNumber
            elif CurNode.isLeaf():
                return -1
            else:
                CurNode = self.getNextChild(CurNode, value)
                
    def getNextChild(self, node, Value):
        numberOfItems = node.getNumberofValues()
        for j in range(numberOfItems):	
            if Value < node.getItemValue(j).value:
                return node.getChild(j)	
            else:	
                return node.getChild(j + 1)
		
    #purpose of this function is to insert the given value in the tree.
    def insert(self,newValue):
        CurNode = self.root
        temp = Data(newValue)
        while True:
            if CurNode.isFull():
                self.split(CurNode)
                CurNode = CurNode.getParent()
                CurNode = self.getNextChild(CurNode, newValue)
            elif CurNode.isLeaf():
                break
            else:
                CurNode = self.getNextChild(CurNode, newValue)
        CurNode.insertValue(temp)
        
    
    #Purpose of this function is to split the given Node.
    def split(self,SNode):
        value = SNode.removeLastValue()
        value1 = SNode.removeLastValue()
        Child = SNode.removeChild(2)	
        Child1 = SNode.removeChild(3)	
        
        new = Node()	
        if SNode == self.root:
            self.root = Node()
            parent = self.root	
            self.root.connectChild(0, SNode)
        else:	
            parent = SNode.getParent()	
            
        Index = parent.insertValue(value1)	
        n = parent.getNumberofValues()
        j = n-1
        while j > Index:	
            temp = parent.removeChild(j)
            parent.connectChild(j+1, temp)	
            j -= 1
        parent.connectChild(Index+1, new)
        
        new.insertValue(value)	
        new.connectChild(0, Child)	
        new.connectChild(1, Child1)	
    def user(self):
        print("a.Insert")
        print("b.search") 
        print("c.display")
        while True:
            user1 = input("Please enter your choice:")
            if (user1 == "a"):
                element = int(input("Enter element to insert:"))
                tree.insert(element)
            if (user1 == "b"):
                element = int(input("Enter element to find:"))
                yes = tree.find(element)
                if yes!= -1:
                    print("Element Found")
                else:
                    print("Element not found")
            if (user1 == "c"):
                tree.displayTree()
            

tree = TwoThreeFourTree()
tree.user()


		

		

		
		
				
			
			
				
		

		
		
		
	
   
        
        
    