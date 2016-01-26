def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
          pivot += 1
          array[i], array[pivot] = array[pivot], array[i]

    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quicksort(array, begin, end):
    if begin >= end:
        return
    pivot = partition(array, begin, end)
    quicksort(array, begin, pivot-1)
    quicksort(array, pivot+1, end)

array = [54,20,31,1,0,7]
print "List before sorting : " , array
quicksort(array, 0, len(array) - 1)
print "List after sorting : " , array