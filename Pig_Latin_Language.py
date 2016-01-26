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



