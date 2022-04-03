def change_position(my_list):

    for i in range(0,len(my_list),2):
            my_list[i],my_list[i+1]=my_list[i+1],my_list[i]
    print(my_list)
          
list1 = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    list1.append(ele)

change_position(list1)