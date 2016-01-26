
def findNumber(a, x, start, end):
  if start > end:
    return  -1
  mid = (start + end) / 2
  if a[mid] == x:
    return mid
  ## Case : 1  if a[start] to a[mid] is sorted , then search first half of array
  if a[start] < a[mid]:
    if (x >= a[start] and x <= a[mid]):
      return findNumber(a, x, start, mid - 1)
    else:
      return findNumber(a,x, mid + 1, end)
  ## Case: 2 if a[start] to a[mid] is not sorted , then a[mid] to a[end] mist be sorted
  else:
    if (x >= a[mid] and x <= a[end]):
      return findNumber(a, x, mid + 1, end)
    else:
      return findNumber(a,x, start, mid -1)


a = [4,5,6,7,0,1,2]
print "Your array is  : " , a
x = input("Enter any number to find in array : ")
result = findNumber(a, x, 0, len(a) - 1)
print "The element is present at %d position: ", result