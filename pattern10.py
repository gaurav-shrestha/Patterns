# Downward Pyramid Pattern
'''
 * * * * *
  * * * *
   * * *
    * *
     *

'''
n =int(input("Enter number of rows: "))
for row in range(n):
    for blank_column in range(row+1):
        print(end=" ")
    for star_column in range(row,n):
        print("*",end=" ")
    print()
