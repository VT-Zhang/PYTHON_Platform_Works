def grade():
    import random
    counter = 0;
    while counter < 10:
        num = int(60 + random.random() * (100-60))
        if num > 59 and num < 70:
            print "Score:",num,"; Your grade is D."
        elif num > 69 and num < 80:
            print "Score:",num,"; Your grade is C."
        elif num > 79 and num < 90:
            print "Score:",num,"; Your grade is B."
        elif num > 89 and num <= 100:
            print "Score:",num,"; Your grade is A."
        counter = counter + 1

grade()
