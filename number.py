
def swap(a,b):
    a , b = b , a
    print "After swapping Number A is :", a
    print "After swapping Number B is :", b

def fibonacci(length):
    a = i =0
    b = 1
    print a
    print b
    while i < length - i:
        c = a + b
        print c
        i = c
        a = b
        b = c
def fibonacci2(length):
    x,y = 0,1
    while y < 50:
        print y
        x,y = y , x+y

a = input("Enter number A :")
b = input("Enter number B :")
swap(a,b)

fibonacci_length = input("Enter length for Fibonacci series: ")
fibonacci(fibonacci_length)
fibonacci2(fibonacci_length)