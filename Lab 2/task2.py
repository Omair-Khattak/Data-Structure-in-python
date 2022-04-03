def Movemin(list1):
    for i in range(0, len(list1)-1):
        min_value = i
        for j in range(i+1, len(list1)):
            if list1[j] < list1[min_value]: #looking for smallest value in list
                min_value = j
        if min_value != i:
            list1[min_value], list1[i] = list1[i], list1[min_value] #swapping 
    return(list1)
def selection_sort(items):
    for i in range(len(items)-1):
        Movemin(items)
def Merge_list(list1, list2): 
    final_list = list1 + list2 
    selection_sort(final_list) 
    return(final_list) 
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
    print(Merge_list(list1,list2)) 
takeinput()
