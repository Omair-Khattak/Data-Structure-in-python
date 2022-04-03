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
        self.size = 0
        
    def push(self, rollNo,year,semister,email):
        new = Student(rollNo, year, semister, email)
        new.next = self.head
        self.head = new
        self.size += 1
        return
        
    def pop(self):
        if self.isEmpty():
            print ("Stack is empty")
            return
        new = self.head
        self.head = self.head.next
        self.size -= 1
        return new
    
    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
            return
        else:
            return (self.head.printStudent())
    
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
        
    def PrintStack(self):         
        curNode=self.head
        while(curNode!=None):
            curNode.printStudent()
            curNode=curNode.next
    def User(self):
            print("""
                  a.push
                  b. Delete items
                  c. Show the number of items
                  d. Find an item
                  e. Print all item
                  f. peek value
                  g. Exit""")
            while True: 
                A = input("Choose the Option::")
                if (A=="a"):
                    rollNo = int(input("Enter roll no as intiger:: "))
                    year = int(input("Enter year as intiger:: "))
                    semister = str(input("Enter semester as string:: "))
                    email = str(input("Enter email as string:: "))
                    studentLinkedList.push(rollNo,year,semister,email)
                elif(A=="b"):
                    studentLinkedList.pop()
                elif(A=="c"):
                    print("The size is:",studentLinkedList.Size())
                elif(A=="d"):
                    studentLinkedList.searchElement()
                elif(A=="e"):
                    studentLinkedList.PrintStack()
                elif(A=="f"):
                    studentLinkedList.peek()
                elif(A=="g"):
                    break

studentLinkedList=StudentLinkedList()
studentLinkedList.User()
          
          


