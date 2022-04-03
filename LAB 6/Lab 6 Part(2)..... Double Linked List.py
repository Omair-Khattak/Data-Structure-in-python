class Student:
    def __init__(self, rollNo,Year, Semister, Email):
        self.rollNo = rollNo
        self.__Year = Year
        self.__Semister = Semister
        self.__Email = Email
        self.next = None
        self.previous = None
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
        
    def addStudentAtStart(self,std): 
        if(self.head == None): 
            self.head = std
            self.tail = std
        else:
            std.next = self.head 
            self.head.previous = std  
            self.head = std                 
    def addAnyPosition(self, p, std): 
        l = self.length()
        temp = self.head
        if(p == 1 and self.head == None):
            self.addStudentAtStart(std)
        elif(l<p):
            print("Out of range")
        else:
            for i in range(p-1):
                temp = temp.next 
            j = temp.next 
            temp.next = std
            std.previous = temp
            std.next = j
            j.previous = std
         

    def addStudentAtEnd(self,std):
        self.tail.next = std
        std.previous = self.tail 
        self.tail = std

    def DeleteFromStart(self):              
        if(self.head == None):
            print("Linked list is empty")
        elif(self.head.next == None):
            self.haed = None
            self.tail = None
        else:
            self.head = self.head.next
            

    def DeleteFromAnyPosition(self, position): 
        l = self.length()
        if(self.head == None):
            print("Sorry Linked List is empty")
        elif(l<position):
            print("Sorry out of range")
        else:
            temp = self.head
            for i in range(position-1):
                temp = temp.next
            pr = temp.previous
            q = temp.next 
            pr.next = q 
            q.previous = pr            

    def DeleteFromEnd(self):
        if(self.tail.previous == None):
            self.DeleteFromStart()
        else:
            temp = self.tail.previous 
            temp.next = None
            self.tail = temp              
    def Previouss(self):
        inputt = int(input("Enter the number to find its previous::"))
        a = self.head.next
        if self.head.getRollNo() == inputt:
            print("no prevoious data exists")
        else:
            while a != None:
                if(a.getRollNo() == inputt):
                    a.previous.printStudent()
                    return
                a = a.next

    def searchElement(self):              
        inp = int(input("enter your number: "))
        currentNode = self.head
        while (currentNode != None):
            if currentNode.getRollNo() == inp: 
                print("The student is valid")  
                return
            currentNode = currentNode.next
        print("Not Found")

    def reverse_move(self): 
        if(self.tail == None):
            print("Linked List is empty")
            return
        temp = self.tail
        while(temp!=None):
            temp.printStudent()
            temp = temp.previous
    def printTotalLinkedList(self):        
        currentNode=self.head
        if(self.head == None):
            print("Empty Linked List")
            return
        while(currentNode!=None):
            currentNode.printStudent()
            currentNode=currentNode.next
    def length(self):
        i = 0
        temp = self.head
        while(temp!=None):
            i = i+1
            temp = temp.next
        return i
studentLinkedList=StudentLinkedList()
std1=Student(4,2030,"3rd semiter","khattak@namal.edu.pk")
std2=Student(3,2050,"7rd semiter","junaid@namal.edu.pk")
std3=Student(2,2023,"5rd semiter","bakht@namal.edu.pk")
std4=Student(1,2031,"2rd semiter","omAIR@namal.edu.pk")
std5=Student(5,2011,"9rd semiter","ghauri@namal.edu.pk")
std6=Student(6,1999,"5th semister","Hadi@namal.edu.pk")

print("Added Elements")
#To add at start
studentLinkedList.addStudentAtStart(std1)
studentLinkedList.addStudentAtStart(std2)
studentLinkedList.addStudentAtStart(std3)
print("After deleted from end ")
#To add at end
studentLinkedList.addStudentAtEnd(std6)
print("")
#To add at any Position
studentLinkedList.addAnyPosition(2,std5)
studentLinkedList.printTotalLinkedList()
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
#To delete at start
# studentLinkedList.DeleteFromStart()
# studentLinkedList.printTotalLinkedList()
# #To delete at end
# studentLinkedList.DeleteFromEnd()
# studentLinkedList.printTotalLinkedList()
# #To delete at any position
studentLinkedList.DeleteFromAnyPosition(2)
studentLinkedList.printTotalLinkedList()
# #To search by roll number
# studentLinkedList.printTotalLinkedList()
# studentLinkedList.searchElement()
# #to print the whole linked list

# #to print the whole list in reverse order
# studentLinkedList.reverse_move()
studentLinkedList.Previouss()





