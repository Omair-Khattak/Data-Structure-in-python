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
    def addStudentAtStart(self,std):             #Add elements at start
        std.next = self.head                    #creating a new node and update the new node next value(std.next)to existing node(self.head)
        self.head = std                         #The new node(std) has been made the head of the linked list which means new node(std) is now the head
    def addAnyPosition(self, previousNode, std): #add elements at any position
        if not previousNode:                     #if previous node is not present
            print("Previous Node does not exist")
            return
        std.next = previousNode.next         #creating a new node(std) and the new node(std) should point the next node
        previousNode.next = std             #previous node will point the new node

    def addStudentAtEnd(self,std):               #add elements at end position
        temp = self.head                         #stores head in temp(variable)
        while temp.next!=None:                   #the loop will not run until the temp is none
            temp = temp.next                     #when temp is none it will move one step further which is End node
        temp.next = std                          #now we found end node so we stored that value(std) at end node

    def DeleteFromStart(self):              #function to delete elements from start
        self.head = self.head.next               #skipping or deleting the Head value

    def DeleteFromAnyPosition(self, position): #function to delete element on given position
        nxtValue = self.head
        prevValue = self.head
        if (nxtValue == position):                 #if given position s at start(head)
            self.DeleteFromStart()            #then call this function to delete it
        while nxtValue!=None:
            if (nxtValue==position):            #if value is present in list
                prevValue.next = nxtValue.next  #skipping or deleting that number
            prevValue = nxtValue                #updating the list values
            nxtValue = nxtValue.next            #updating the list value

    def DeleteFromEnd(self):
        temp = self.head
        while temp.next.next!=None:        #loop for finding the second last element
            temp = temp.next               #storing the last value in temp
        temp.next = None                   #Deleting the last element

    def searchElement(self):               #search element by roll no
        inp = int(input("enter your number: "))
        currentNode = self.head
        while (currentNode != None):
            if currentNode.getRollNo() == inp: #if roll no is present
                print("The student is valid")  #print this this statement
                return
            elif(currentNode.next==None):      #if roll no is not present
                print("The student is not valid") #print this statement
            currentNode = currentNode.next

    def reverse_move(self):
        previous = None              #set privious as None
        current = self.head          #set current as Head
        while current != None:       #Loop will run until current is not none
            nxxt = current.next      #make a variable as nxxt and give the value of next of current
            current.next = previous  #set next of current to the previous
            previous = current       #and privious to the current
            current = nxxt           #Now current should be set to nxxt
        self.head = previous         #set head to previous

    def printTotalLinkedList(self):         #Function to print the whole liinked list
        currentNode=self.head
        while(currentNode!=None):
            currentNode.printStudent()
            currentNode=currentNode.next

studentLinkedList=StudentLinkedList()
std1=Student(4,2030,"3rd semiter","khattak@namal.edu.pk")
std2=Student(3,2050,"7rd semiter","junaid@namal.edu.pk")
std3=Student(2,2023,"5rd semiter","bakht@namal.edu.pk")
std4=Student(1,2031,"2rd semiter","omAIR@namal.edu.pk")
std5=Student(5,2011,"9rd semiter","ghauri@namal.edu.pk")
std6=Student(6,1999,"5th semister","Hadi@namal.edu.pk")

#To add at start
studentLinkedList.addStudentAtStart(std1)
studentLinkedList.addStudentAtStart(std2)
studentLinkedList.addStudentAtStart(std5)
#To add at end
studentLinkedList.addStudentAtEnd(std3)
studentLinkedList.addStudentAtEnd(std4)
#To add at any Position
studentLinkedList.addAnyPosition(studentLinkedList.head.next,std6)
#To delete at start
studentLinkedList.DeleteFromStart()
#To delete at end
studentLinkedList.DeleteFromEnd()
#To delete at any position
studentLinkedList.DeleteFromAnyPosition(std1)
#To search by roll number
studentLinkedList.printTotalLinkedList()
studentLinkedList.searchElement()
#to print the whole linked list
print("")
print("To print the linked list in reverse order: \n")
studentLinkedList.reverse_move()
#to print the whole list in reverse order
studentLinkedList.printTotalLinkedList()

