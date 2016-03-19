def cpio (x,lo,hi):

    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    #return max(max(x,lo) , max(x,hi) , x)
    return min(max(x, lo), hi)

ans = cpio(5,6,7)
print ans


