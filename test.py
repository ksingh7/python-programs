
a = [0,1,2]
b = [3,4,5]

print "Value of a and b before swaping :"
print "value of a :" , a
print "value of b :" , b

print "\nswap in two line"

a[0] = b[0]
b[0] = a[0]

print "value of a :" , a
print "value of b :" , b




print "\nswap in one line"

# Reinitilizing value of a and b before performing swaping

a = [0,1,2]
b = [3,4,5]

a[0], b[0] = b[0], a[0]

print "value of a :" , a
print "value of b :" , b


