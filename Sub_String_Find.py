s = 'ebobbobblbooblvyboyboabobbhqjbobb'
substr = 'bob'
count = 0
start = 0
while True:
    start = s.find(substr,start)
    if start == -1:
        break
    count += 1
    start = start + (len(substr)-1)
print "Number of times bob occurs is:", count
