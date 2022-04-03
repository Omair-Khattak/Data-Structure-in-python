def displaysublist(A):  
   B = [[ ]] 
       
   for i in range(len(A) + 1):     
      for j in range(i + 1, len(A) + 1):         
         sublist = A[i:j] 
         B.append(sublist) 
   return B 
A= []
n=int(input("Enter the size of list:"))
print("Enter the Elements in list:")
for i in range(int(n)):
   inp=int(input(""))
   A.append(inp)
print("Sublist :",displaysublist(A))