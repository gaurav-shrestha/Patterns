# Butterfly
"""

*           * 
* *       * *
* * *   * * *
* * * * * * *
* * *   * * *
* *       * *
*           *

"""

n= int(input("Enter number of upper-half rows: "))

# Upper part
for i in range(n-1):
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i,n-1):
        print(" ",end=" ")
    for j in range(i,n-1-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()


# Lower part
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    for j in range(i):
        print(" ",end=" ")
    for j in range(i-1):
        print(" ",end=" ")
    if i==0:
        for j in range(i,n-1):
            print("*",end=" ")
    else:
        for j in range(i,n):
            print("*",end=" ")
    print()