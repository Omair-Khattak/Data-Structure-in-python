class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
    def printStack(self):
           return (self.data)
class Stack:
    def __init__(self):
        self.head = None
 
    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
 
    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped
    def printTotalLinkedList(self):        
        cur=self.head
        if(self.head == None):
            print("Empty Linked List")
            return
        while(cur!=None):
            cur.printStack()
            cur=cur.next
 
aStack = Stack()
aStack.push(20)
aStack.push(30)
aStack.printTotalLinkedList()