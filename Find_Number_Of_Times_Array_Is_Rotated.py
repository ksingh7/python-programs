'''
Suppose a sorted array [0 1 2 4 5 6 7]is rotated and it become [4 5 6 7 0 1 2].
Find how many times this array is rotated
'''

def findNumRotation(num):
    L = 0; R = len (num) -1
    while L <R and num [L]> num [R]:
        M = (L + R) / 2
        if num [M] < num [R]:
          R = M
        else :
          L = M + 1
    return L

#a = [4,5,6,7,0,1,2]
a = [7,0,1,2,4,5,6]
print "Your array is  : " , a
result = findNumRotation(a)
print "The array is rotated %d times " % result