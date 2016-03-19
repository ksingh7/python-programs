def binary_TO_decimal(bin_num):
    power = len(bin_num) -1
    total = 0
    for i in range(len(bin_num)):
        total = total + int(bin_num[i]) * (2 ** power)
        power -= 1
    print "Binary number: " , total

bin_num = raw_input("Enter Binary Number that needs to be converted to Decimal : ")
binary_TO_decimal(bin_num)