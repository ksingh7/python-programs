def binarySearch(a, num):
    start = 0
    end = len(a) -1
    while (start <= end):
      mid = (start + end ) / 2
      if a[mid] == num:
          return mid
      elif a[mid] > num:
          start = 0
          end = mid -1
      elif a[mid] < num:
          start = mid + 1
          end = end
    return  -1

a = [0,1,2,3,4,5,6,7,8,9]
print "Your array is  : " , a
num = input("Enter number to search its position : ")
result = binarySearch(a, num)
if result > 0:
  print "The position of %d in array is %d" % (num, result)
else:
  print "element not found"