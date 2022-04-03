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
        
class CircularStudentLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def enqueue(self, rollNo,Year, Semister, Email):
        element = Student(rollNo,Year, Semister, Email)
        if self.tail != None:
            self.tail.next = element
        else:
            self.head = element

        self.tail = element
        element.next = self.head
        self. size += 1
        return self.tail
    def dequeue(self):
        if self.head != None:
            delete= self.head
            self.head = self.head.next
            self.size -= 1
        else:
            delete = None
            print("Circular is empty !!")
        return delete
    
    def isEmpty(self):
        first = self.head
        last  = self.tail
        if first == None and last == None:
            return True
        else:
            return False
        
    def Size(self):
        return self.size
    
    def searchElement(self):    
        current = self.head  
        flag = False
        element = int(input("input roll no::"))
        if(self.head == None):    
            print("List is empty")
            return
        while(True):      
                if(current.getRollNo() ==  element):    
                    flag = True
                    break
                current = current.next 
                if(current == self.head):    
                    break
        if(flag):
            print("number is present in circular list")  
        else:
            print("number is not not present in circular list")
                     
    def display(self):    
        if self.isEmpty():
            print("stack is empty")
            return
        front = self.head
        back  = self.tail
        if front != None and back != None:
            while back != front:
                front.printStudent()
                front = front.next
            back.printStudent()
            
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
                    studentLinkedList.display()
                elif(A=="f"):
                    break

studentLinkedList=CircularStudentLinkedList()
studentLinkedList.User()



