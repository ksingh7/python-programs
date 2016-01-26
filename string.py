def countChar(string):
    wc = 0
    for i in range(len(string)):
        if string[i] == ' ' or string[i] == '\t' or string[i] == '\n':
                wc += 1
    return (len(string) - wc)

def reverseString(string):
    return string[::-1]

def reverseString2(word):
    import sys
    for char in range((len(word)-1),-1,-1):
        sys.stdout.write(word[char])

def countRepeatingWords(string):
    for i in range(len(string)):
        count = 0
        for j in range(len(string)):
            if string[i] == string[j]:
               count += 1
        print "Total count for word " + string[i] + " is :", count

def stringFirstLast(string):
    if len(string) < 2:
        return "String too small"
    else:
        print "String from first and last characters is :", string[0:2] + string[-2:]


def change_char(str1):
  char = str1[0]
  length = len(str1)
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]
  print str1


def characterMixUP(string1,string2):
    string1_extract = string1[:2]
    string2_extract = string2[:2]
    string3 = string2_extract + string1[2:] + " " + string1_extract + string2[2:]
    print string3


def not_poor(str1):
  snot = str1.find('not')
  sbad = str1.find('poor')
  if sbad > snot:
    str1 = str1.replace(str1[snot:(sbad+4)], 'good')
  return str1


def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]

def countOccouranceOfWord(string):
    count = dict()
    words = string.split()
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    #print count
    print sorted(count.items(), key=lambda x: x[1])

def countOccouranceOfCharacters(string):
    count = dict()
    for char in string:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    print count

def Mostrepeatingwords(string):
    from collections import Counter
    counter = Counter(string.split())
    print sorted(counter.items(), key=lambda x: x[1])[-3:]

def countOccouranceOfCharacters_2(string):
    from collections import Counter
    counter = Counter(string)
    for char in string:
        print char + ":" + str(counter[char])

def PigLatin(paragraph):
    count = 0
    words = paragraph.split()
    for word in words:
        count += 1
        word = word.lower()
        for i in "aeiou":
            if word.startswith(i):
                word = word[1:] + word[0] + "ni" + "j" * count
        if not word.endswith("j"):
            word = word + "ni" + "j" * count
        print word

print("Enter your string ")
string = raw_input()
#print "Number of words in your string are : " , countChar(string)
#print "After reversing the string, your new string would be :", reverseString(string)
#print "Counting occurrence of each character:"
#countRepeatingWords(string)
#print "Another way of reversing string is : "
#reverseString2(string)
#stringFirstLast(string)
#change_char("restart")
#characterMixUP("abc","xyz")
#print(not_poor('The lyrics is not that poor!'))
#print(find_longest_word(["PHP", "Exercises", "Backend"]))
#countOccouranceOfWord(string)
#countOccouranceOfCharacters("heera")
#Mostrepeatingwords(string)
#countOccouranceOfCharacters_2(string)
paragraph = "This is just an example"
PigLatin(paragraph)

