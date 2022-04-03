class Job:
    def __init__(self, name, priority):
        self.__name = name
        self.priority = priority
        self.next = None
    def getName(self):
        return self.__name
    def Print(self):
        print(self.getName())

class PriorityQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def isEmpty(self):
        if self.front == None:
            return

    def enqueue(self, name, priority):
        newNode = Job(name, priority)
        if not self.rear:
            self.front = newNode
            self.rear = newNode
            self. size += 1
            return
        if self.front.priority < newNode.priority:
            newNode.next = self.front
            self.front = newNode
            self. size += 1
            return
        previous = None
        current = self.front
        while(current and newNode.priority < current.priority):
            previous = current
            current = current.next
            

        if current:
            previous.next = newNode
            newNode.next = current
            self. size += 1
        else:
            self.rear.next = newNode
            self.rear = newNode
        

    def dequeue(self):
        if self.isEmpty():
            print('Queue is empty')
            return
        temp = self.front
        self.front = self.front.next
        if self.front == None:
            self.rear = None
        self.size -= 1
        return temp.getName()
        
    def Size(self):
        return self.size
    
    def PrintQueue(self):    
        if self.isEmpty():
            print("stack is empty")
            return
        currentNode=self.front
        while(currentNode!=None):
            currentNode.Print()
            currentNode=currentNode.next
    def searchElement(self):              
        inp = str(input("Enter job name to search: "))
        curNode = self.front
        while (curNode != None):
            if curNode.getName() == inp: 
                print("The student is valid") 
                return
            elif(curNode.next==None):      
                print("The student is not valid")
            curNode = curNode.next
            
    def User(self):
            print("""
                  a. Enqueue 
                  b. Delete items 
                  c. Show the number of items 
                  d. Find an item 
                  e. Print all items
                  f. Exit """)
            while True: 
                A = input("Choose the Option::")
                if (A=="a"):
                    name = str(input("Enter Name of Job as String:: "))
                    pririty = int(input("Enter priority as intiger:: "))
                    priority.enqueue(name,pririty)
                elif(A=="b"):
                    priority.dequeue()
                elif(A=="c"):
                   print("The size is:",priority.Size())
                elif(A=="d"):
                   priority.searchElement()
                elif(A=="e"):
                    priority.PrintQueue()
                elif(A=="f"):
                    break
priority = PriorityQueue()
priority.User()