
def linearSearch(a, num):
    for i in range(0, len(a) - 1):
        if a[i] == num:
            return i
    return -1


a = [54,26,93,17,77,31,44,55,20,31,45,90,111,1,0,7]
print "Your array is  : " , a
num = input("Enter number to search its position : ")
result = linearSearch(a, num)
if result > 0:
    print "The position of %d in array is %d" % (num, result)
else:
    print "element not found"



