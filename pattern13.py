# Sand-glass
'''

 * * * * * 
  * * * *  
   * * *   
    * *    
     *
    * *
   * * *
  * * * *
 * * * * *

'''
n=int(input("Enter number of rows of upper half: "))
for i in range(n-1):
    for j in range(i+1):
        print(end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i,n):
        print(end=" ")
    for i in range(i+1):
        print("*",end=" ")
    print()