def unique(list1):
    unique_list = []
    lis = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    for x in unique_list:
        lis.append(x)
    print(lis)

list1 = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
            ele = int(input())
            list1.append(ele)
print("the unique values from list is")
unique(list1)
