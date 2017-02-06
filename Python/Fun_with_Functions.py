def odd_even(a,b):
    for num in range (a,b):
        if num % 2 != 0:
            print "Number is",num,". This is an odd numer."
        else:
            print "Number is",num,". This is an even numer."

odd_even(1,21)

def multiply(list, b):
    i = 0
    for num in list:
        list[i] = num * b
        i = i + 1
    return list
print multiply([2,4,10,16], 5)
