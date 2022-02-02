# Reverse Hill Pattern printing by taking input from user
''' 

 * * * * * * * * *
   * * * * * * *
     * * * * *
       * * * 
         *

'''
n=int(input("Enter number of Rows: "))
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()