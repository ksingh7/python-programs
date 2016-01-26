def Quicksort(a, start, end):
    if start < end:
        p = partition(a, start, end)
        Quicksort(a, start, p-1)
        Quicksort(a, p+1, end)
        return  a

def partition(a, start, end):
    divider = start
    pivot = end
    for i in range(start, end):
        if a[i] < a[pivot]:
          a[i] , a[divider] = a[divider], a[i]
          divider += 1

    a[divider], a[pivot] = a[pivot], a[divider]
    return divider


a = [54,26,1,0,7,43,23,11,2,1,3]
print "List before sorting : " , a
Result = Quicksort(a, 0, len(a)-1)
print "List after sorting : " , Result



