def binSearch(ary, elem):
    def recurse(first, last):
        mid = (first + last) / 2
        if first > last:
            return None
        elif (ary[mid] < elem):
            return recurse(mid + 1, last)
        elif (ary[mid] > elem):
            return recurse(first, mid - 1)
        else:
            return mid

    return recurse(0, len(ary)-1)

a = [0,1,2,3,4,5,6,7,8,9]
print "Your array is  : " , a
num = input("Enter number to search its position : ")
result = binSearch(a,num)
if result > 0:
  print "The position of %d in array is %d" % (num, result)
else:
  print "element not found"


