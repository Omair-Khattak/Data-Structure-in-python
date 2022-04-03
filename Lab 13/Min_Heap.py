class Min_Heap:
    def __init__(self):
        self.heap_list = ["Min-Heap==>"]
        self.current_size = 0
 
    def shift_up(self, index):
        while index // 2 > 0:
            if self.heap_list[index] < self.heap_list[index // 2]:
                self.heap_list[index], self.heap_list[index // 2] = self.heap_list[index // 2], self.heap_list[index]
            index = index // 2
    
    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.shift_up(self.current_size)
        
    def shift_down(self, index):
        while (index * 2) <= self.current_size:
            a = self.min_child(index)
            if self.heap_list[index] > self.heap_list[a]:
                self.heap_list[index], self.heap_list[a] = self.heap_list[a], self.heap_list[index]
            index = a
            
    def min_child(self, index):
        if (index * 2)+1 > self.current_size:
            return index * 2
        else:
            if self.heap_list[index*2] < self.heap_list[(index*2)+1]:
                return index * 2
            else:
                return (index * 2) + 1
    
   
    def delete(self):
        if len(self.heap_list) == 1:
            print("Heap is empty")
 
        firstIndex = self.heap_list[1]
 
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop() # Pop the last value we know that a copy was set on the root
        self.shift_down(1)
 
        return firstIndex
    
    def Print(self):
       print(self.heap_list)
       
    
    def search(self,value):
        if value in self.heap_list:
            print("Found")
        else:
            print("Not found")
        
    def user(self):
        print("a.Insert")
        print("b.delete") 
        print("c.display")
        print("d.search")
        while True:
            user1 = input("Please enter your choice:")
            if (user1 == "a"):
                element = int(input("Enter element to insert:"))
                Heaptree.insert(element)
            if (user1 == "b"):
               (Heaptree.delete())  
            if (user1 == "c"):
                Heaptree.Print()
            if (user1 == "d"):
                element = int(input("Enter element you want to find:"))
                Heaptree.search(element)
        
Heaptree = Min_Heap()   
Heaptree.user()