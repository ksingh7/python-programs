def guessNumber():
    low = 0
    high = 100
    guess = 0
    while low < high:
        mid = (low + high) / 2
        print "Is your secret number " + str(mid) + "?"
        response = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.  ")
        if response == 'c' or response == 'C':
            print "Game over. Your secret number was: ", mid
            break
        elif response == 'h' or response == 'H':
            high = mid
        elif response == 'l' or response == 'L':
            low = mid
        else:
            for i in 'cChHlL':
                if response != i:
                    print "Sorry, I did not understand your input."
                    break



print "Please think of a number between 0 and 100!"
guessNumber()

