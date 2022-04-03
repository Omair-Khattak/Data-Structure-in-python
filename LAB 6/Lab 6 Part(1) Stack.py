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
        self.size = 0
        
    def push(self, element):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node 
        self.size += 1
        
    def pop(self):
        if self.isEmpty():
            print ("Stack is empty")
            return
        pop = self.head
        self.head = self.head.next
        self.size -= 1
        return pop
    
    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
            return
        return (self.head.printNode())
    
    def isEmpty(self):
        if self.head is None:
            return True 
        else:
            return False
        
    def Size(self):
        return self.size
        
    def PrintStack(self):         
        currentNode=self.head
        while(currentNode!=None):
            currentNode.printNode()
            currentNode=currentNode.next

studentLinkedList=StudentLinkedList()
print("Pushed Elements:")
studentLinkedList.push(10)
studentLinkedList.push(11)
studentLinkedList.push(20)
studentLinkedList.push(100)
studentLinkedList.push(200)
studentLinkedList.PrintStack()
print("After Popped:")
studentLinkedList.pop()
studentLinkedList.pop()
studentLinkedList.PrintStack()
print("The peak value is:")
studentLinkedList.peek()
print("Size of the linked list is:",studentLinkedList.Size())
studentLinkedList.push(30)
studentLinkedList.push(35)
studentLinkedList.PrintStack()

