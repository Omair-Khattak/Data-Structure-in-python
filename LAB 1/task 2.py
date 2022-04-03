def common_data(list1, list2):
    result = []

    for x in list1:
        for y in list2:
            if x == y:
                result.append(y)
    print("The common elements are:",result)
a = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
        ele = int(input())
        a.append(ele)
b = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
        ele = int(input())
        b.append(ele)
common_data(a, b)

