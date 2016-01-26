def passwordChecker(string):
    import re
    x = True
    while x:
        if (len(string) < 6 or len(string) > 12):
            print "Incorrect length"
            break
        elif not (re.search('[a-z]',string)):
            print "no lower case characters found"
            break
        elif not (re.search('[A-Z]',string)):
            print "no upper case characters found"
            break
        elif not (re.search('[@$#]',string)):
            print "no special characters found"
            break
        else:
            print "Password validated successfully"
            x = False
            break

password = raw_input("Enter password to validate")
passwordChecker(password)
