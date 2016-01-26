'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.
'''

def findMin(num):
    L = 0; R = len (num) -1
    while L <R and num [L]> num [R]:
        M = (L + R) / 2
        if num [M] < num [R]:
          R = M
        else :
          L = M + 1
    return num [L]

a = [4,5,6,7,0,1,2]
print "Your array is  : " , a
result = findMin(a)
print "The minimum element of array is: ", result
