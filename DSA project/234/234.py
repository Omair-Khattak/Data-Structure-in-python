class Data:
    def __init__(self,dataValue):
        self.value=dataValue[0][1]
        self.fullData=dataValue

    def getData(self):
        return self.value

    def getFullData(self):
        return self.fullData   

class Node:
    maxNumberofChildren=4

    def __init__(self):
        self.numberOfItems=0
        self.items=[]
        self.children=[]
        self.parent=None
        for i in range(self.maxNumberofChildren):
            self.children.append(None)
        for j in range(self.maxNumberofChildren-1):
            self.items.append(None)

    def getParent(self):
        return self.parent

    def getChild(self, index):
        return self.children[index]

    def getItemValue(self, index):
        return self.items[index]

    def getNumberofValues(self):
        return self.numberOfItems

    def isFull(self):
        if self.numberOfItems== self.maxNumberofChildren-1:
            return True
        return False

    def isLeaf(self):
        return not self.children[0]

    def findValue(self,valuetoBeFound):
        for i in range(self.maxNumberofChildren-1):
            if self.items[i]!=None:
                if self.items[i].value==valuetoBeFound:
                    return i
        return -1

    def connectChild (self,childNumber, child):
        self.children[childNumber]=child
        if child:
            child.parent=self

    def displayNode(self):
        for i in range(self.numberOfItems):
            if self.items[i] != None:
                print('/',self.items[i].getFullData(),end=" ")
        print('\n')

    def removeLastValue(self):
        temp=self.items[self.numberOfItems-1]
        self.items[self.numberOfItems-1]=None
        self.numberOfItems-=1
        return temp

    def removeChild(self, childNumber):
        tempChild=self.children[childNumber]
        self.children[childNumber]=None
        return tempChild

    def insertValue (self,newData):
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

class TwoThreeFourTree:

    def __init__(self):
        self.root=Node()

    def displayTree(self,current):
        current.displayNode()
        items = current.getNumberofValues()
        for i in range(items+1):
            temp = current.getChild(i)
            if temp:
                self.displayTree(temp)
            else:
                return

    def find(self,value):
        temp = self.root
        while True:
            childNumber = temp.findValue(value)
            if childNumber != -1:
                return temp.items[childNumber].fullData
            elif temp.isLeaf():
                return False 
            else: 
                temp = self.nextChild(temp, value)

    def insert(self,data):
        current = self.root
        while True:
            if current.isFull():
                self.split(current)
                current = current.getParent()
                current = self.nextChild(current, data[0][1])
            elif current.isLeaf():
                break
            else:
                current = self.nextChild(current, data[0][1])
        current.insertValue(Data(data))

    def nextChild(self,current,value):
        for j in range(current.getNumberofValues()):
	        if value < current.getItemValue(j).value:	
	            return current.getChild(j)
            else:
                 return current.getChild(j + 1)

    def split(self,SNode):
        item3 = SNode.removeLastValue()	
        item2 = SNode.removeLastValue()	
        child2 = SNode.removeChild(2)	
        child3 = SNode.removeChild(3)	
        temp = Node()
        if SNode == self.root:
            self.root = Node()
            current = self.root	
            self.root.connectChild(0, SNode)
        else:	
            current = SNode.getParent()

        itemIndex = current.insertValue(item2)	
        totalValues = current.getNumberofValues()	
        iteration = totalValues-1
        while iteration > itemIndex:	
            pTemp = current.removeChild(iteration)
            current.connectChild(iteration+1, pTemp)	
            iteration -= 1
        current.connectChild(itemIndex+1, temp)

        temp.insertValue(item3)	
        temp.connectChild(0, child2)	
        temp.connectChild(1, child3)	


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

tree234 = TwoThreeFourTree()
for i in data2:
    tree234.insert(i)


print("a. Movie Having MAXIMUM rating"
"\n""b. Movie Having SAME rating"
"\n""c. Movie Having MINIMUM rating"
"\n""d. Exit (stop the program)")


while True:
    choice=input("enter choice from a to d: ")
    if choice=="a":
        result = tree234.find(10.0)
        if result:
            print(result)
        else:
            print("Value not found")
    
    elif choice=="b":
        num=float(input("Enter average rating to know number of movies having same ratings: "))
        result = tree234.find(num)
        if result:
            print(len(result))
        else:
            print("Value not found") 
   
    elif choice=="c":
        result = tree234.find(1.0)
        if result:
            print(result)
        else:
            print("Value not found")
   
    elif choice=="d":
        print("program is stop")
        break
      
    else:
        print("invalid input") 







