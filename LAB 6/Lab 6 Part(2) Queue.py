class Student:
    def __init__(self, rollNo,Year, Semister, Email):
        self.rollNo = rollNo
        self.__Year = Year
        self.__Semister = Semister
        self.__Email = Email
        self.next = None
    def getRollNo(self):
        return self.rollNo
    def getYear(self):
        return self.__Year
    def getSemister(self):
        return self.__Semister
    def getEmail(self):
        return self.__Email
    def printStudent(self):
        print(self.getRollNo(), self.getYear(), self.getSemister(), self.getEmail())
        
class StudentLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size = 0
        
    def enqueue(self,rollNo,year,semister,email):
        new = Student(rollNo,year,semister,email)
        if self.isEmpty():
            self. head = new
        else:
            self. tail. next = new
        self. tail = new
        self. size += 1
        
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
            currentNode.printStudent()
            currentNode=currentNode.next
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
                    rollNo = int(input("Enter roll no as intiger:: "))
                    year = int(input("Enter year as intiger:: "))
                    semister = str(input("Enter semester as string:: "))
                    email = str(input("Enter email as string:: "))
                    studentLinkedList.enqueue(rollNo,year,semister,email)
                elif(A=="b"):
                    studentLinkedList.dequeue()
                elif(A=="c"):
                    print("The size is:",studentLinkedList.Size())
                elif(A=="d"):
                    studentLinkedList.searchElement()
                elif(A=="e"):
                    studentLinkedList.PrintQueue()
                elif(A=="f"):
                    break

studentLinkedList=StudentLinkedList()
studentLinkedList.User()



