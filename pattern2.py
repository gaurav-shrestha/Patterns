#Increasing Triangle    --Basic
'''

i=0  *
i=1  * *
i=2  * * *
i=3  * * * *
i=4  * * * * *

'''

n=5
for i in range(n):          # Rows
# for i in range(0,n):
    for j in range(i+1):    # Columns
    # for j in range(0,i+1):
        print("*",end=" ")
    print()