'''
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''

def arrow(n):
    for i in range(n):
        for j in range(i):
            print '*',
        print ' '
    for i in range(n,0,-1):
        for j in range(i):
            print '*',
        print ' '
'''
*
**
***
****
*****
****
***
**
*
'''
def arrow2(n):
    for i in range(n):
        s = '*' * i
        print s
    for i in range(n,0,-1):
        s = '*' * i
        print s

'''
    *
   ***
  *****
 *******
'''
def triangle(n):
    for i in range(n):
        s=' '* (n-i)
        s= s + '*'* (i*2-1)
        print s



n = input("Enter the depth :")
arrow2(n)
arrow(n)
triangle(n)
