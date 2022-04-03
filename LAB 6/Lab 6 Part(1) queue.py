class Node:
    def __init__(self, data):
        self.__data =data
        self.next = None
    def getdata(self):
        return self.__data
    def printNode(self):
        print(self.getdata())

class StudentLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size = 0
        
    def enqueue(self,element):
        new = Node(element)
        if self.isEmpty():
            self. head = new
        else:
            self.tail.next = new
        self.tail = new
        self.size += 1
        
    def dequeue(self):
        if self.isEmpty():
            print("stack is empty")
        self. head = self. head. next
        self.size -= 1
        if self.isEmpty:
            self.tail = None 
    
    def isEmpty(self):
        if self.head is None:
            return True 
        else:
            return False
        
    def Size(self):
        return self.size
    
    def searchElement(self):              
        inp = int(input("Enter roll No number: "))
        curNode = self.head
        while (curNode != None):
            if curNode.getRollNo() == inp: 
                print("The student is valid") 
                return
            elif(curNode.next==None):      
                print("The student is not valid")
            curNode = curNode.next
        
    def PrintQueue(self):    
        if self.isEmpty():
            print("stack is empty")
            return
        currentNode=self.head
        while(currentNode!=None):
            currentNode.printNode()
            currentNode=currentNode.next
            
studentLinkedList=StudentLinkedList()
studentLinkedList=StudentLinkedList()
print("enqueued Elements:")
studentLinkedList.enqueue(10)
studentLinkedList.enqueue(11)
studentLinkedList.enqueue(20)
studentLinkedList.enqueue(100)
studentLinkedList.enqueue(200)
studentLinkedList.PrintQueue()
print("After dequeqed:")
studentLinkedList.dequeue()
studentLinkedList.dequeue()
studentLinkedList.PrintQueue()
print("Size of the linked list is:",studentLinkedList.Size())
