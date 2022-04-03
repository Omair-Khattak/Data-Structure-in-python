class QuadraticProbing:
    def __init__(self,size):
        self.lenght = size
        self.table = [0 for i in range(self.lenght)]

    def hashIndex(self,num):
        for i in range(self.lenght):
            index = (num%self.lenght +(i*i)) % self.lenght
            if self.table[index] == 0:
                return index

    def insert(self,num):
        index = self.hashIndex(int(num[0][1]*10))
        self.table[index]=num

    def search(self,num):
        for i in range(self.lenght):
            index = (int(num*10)%self.lenght + (i*i)) % self.lenght
            if self.table[index][0][1] == num:
                return [True,self.table[index]]
        return [False]        

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
length = 97
hashing = QuadraticProbing(length)
for i in data2:
    hashing.insert(i)


print("a. Movie Having MAXIMUM rating"
"\n""b. Movie Having SAME rating"
"\n""c. Movie Having MINIMUM rating"
"\n""d. Exit (stop the program)")


while True:
    choice=input("enter choice from a to d: ")
    if choice=="a":
        print(hashing.search(10.0)[1])
    
    elif choice=="b":
        num=float(input("Enter average rating to know number of movies having same ratings: "))
        print(len(hashing.search(num)[1]))  
   
    elif choice=="c":
        print(hashing.search(1.0)[1])
   
    elif choice=="d":
        print("program is stop")
        break
      
    else:
        print("invalid input") 


