def fractionTObinary(num):
    power = 0
    x = num
    while (((2 ** power) * num) % 1) != 0: # Convert fraction number to whole number
        print('Remainder = ' + str((2**power)*num - int((2**power)*num)))
        power += 1   # Find the minimum power of 2 , such that when its multiplied to fraction number
                     # the number becomes whole number

    num = int(num * (2 ** power))  # Convert fraction number to decimal whole number

    result = ''
    if num == 0:
        result = '0'
    while num > 0:
        result = str(num % 2) + result
        num = num / 2

    for i in range(power - len(result)):
        result = '0' + result

    result = result[0:-power] + '.' + result[-power:]
    print "The Binary equivalent of " + str(x) + " is " + str(result)


frac_num = float(raw_input("Enter Fraction Number that needs to be converted to Binary : "))
fractionTObinary(frac_num)