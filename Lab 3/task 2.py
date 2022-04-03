def insert(list1,index):
        sortValue = list1[index]
        pos = index
        while list1[pos-1] > sortValue and pos>0:  
            list1[pos], list1[pos-1] = list1[pos-1], list1[pos]
            pos = pos -1
        list1[pos] = sortValue
        print(list1)
        return(list1)
def insertion_sort(list1,list2):
    count = 0
    total = list1 + list2
    for i in range(len(list1),len(total)):
        total = insert(total,i)
        count = count+1
    print("The number of steps taken:",count,"steps")
    return total
def takeinput():
    list1 = []
    list2 = []
    range_of_list1 = int(input("Enter the range of first list:")) 
    range_of_list2 = int(input("Enter the range of second list:")) 
    for i in range(range_of_list1):
        value = int(input("enter the numbers of first list:"))
        list1.append(value)
    print("this is list1 elements:",list1)
    for i in range(range_of_list2):
        value = int(input("enter the numbers of second list:"))
        list2.append(value)
    print("this is list2 elements:",list2)
    insertion_sort(list1,list2)
takeinput()