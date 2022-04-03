def insert(list1):
    for i in range(1, len(list1)):
        sortValue = list1[i]
        while list1[i-1] > sortValue and i>0:  
            list1[i], list1[i-1] = list1[i-1], list1[i]
            i = i -1
    return list1
def insertion_sort(list1,list2):
    total = list1 + list2 
    print(insert(total)) 
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