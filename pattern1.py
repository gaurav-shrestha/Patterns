# Printing Square  --Basic
"""

    * * * * *
    * * * * *
    * * * * *
    * * * * *

"""

a=int(input("Enter number of rows:"))
for i in range(a):
# Equivalent to 
# for i in range(0,a):
# for i in range(1,a+1):
    for j in range (a):         # First look this logic
        print('*',end=' ')      # It will print the character rowwise so one "*" is printed in one row as given logic. 
        # To print all stars in same row we used end parameter.
    print()