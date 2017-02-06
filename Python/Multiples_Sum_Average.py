for num in range(1, 1001):
    print num

for num in range(5, 101):
    if num % 5 == 0:
        print num

a = [1, 2, 5, 10, 255, 3]
sum = 0
for num in a:
    sum = sum + num
print sum


b = [1, 2, 5, 10, 255, 3]
sum = 0
for num in b:
    sum = sum + num
avg = sum/len(b)
print avg
