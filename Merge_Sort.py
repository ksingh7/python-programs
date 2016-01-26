def Mergsort(A):
    n = len(A)
    if n > 1:
      mid = n / 2
      Left = A[:mid]
      Right = A[mid:]
      Mergsort(Left)
      Mergsort(Right)
      Merge(Left,Right,A)
      return A

def Merge(L,R,A):
    i,j,k = 0,0,0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1

a = [54,26,93,17,77,31,44,55,20,31,45,90,111,1,0,7]
print "List before sorting : " , a
Result = Mergsort(a)
print "List after sorting : " , Result


