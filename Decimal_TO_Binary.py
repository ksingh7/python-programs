def decimal_TO_binary(num):
    answer = ''
    if num < 0:
        num = abs(num)
        isNeg = True
    else:
        isNeg = False
    while num > 0:
        result = num % 2
        num = num / 2
        answer = answer + str(result)
    if isNeg:
        print '- ' + answer
    else:
        print answer

dec_num = input("Enter Decimal Number that needs to be converted to Binary : ")
decimal_TO_binary(dec_num)