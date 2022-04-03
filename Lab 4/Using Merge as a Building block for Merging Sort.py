def Merge(L_list, R_list):
    Final_list = []
    i = 0
    j = 0
    while i < len(L_list) and j < len(R_list):
        if (L_list[i] <= R_list[j]):
            Final_list.append(L_list[i])
            i = i+1
        else:
            Final_list.append(R_list[j])
            j = j+1
    Final_list += L_list[i:] 
    Final_list += R_list[j:] 
    return Final_list

def MergeSort(list1):
    if (len(list1)<=1):
        return list1
    half = len(list1)//2
    L_list = MergeSort(list1[:half])
    R_list =MergeSort(list1[half:])
    return Merge(L_list, R_list)

def takeinput():
    list1 = []
    num = int(input("How many numbers do you want in your list: "))
    for i in range(num):
        inputt = int(input("Enter the number:"))
        list1.append(inputt)
    print("your Sorted list is:",MergeSort(list1))
takeinput()