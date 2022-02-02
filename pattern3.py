# Decreasing Triangle    --Basic
'''

0(i) to 5(n)  * * * * *
1(i) to 5(n)  * * * *
2(i) to 5(n)  * * *
3(i) to 5(n)  * *
4(i) to 5(n)  *

'''

n=5
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()