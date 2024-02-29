import math
numbers = list (range (0, 21))
#squared_even_numbers = [x**0.5 for x in numbers if x % 2 ==0]
squared_even_numbers = [math.sqrt(x) for x in numbers if x % 2 == 0]
print(numbers, squared_even_numbers)
for n in squared_even_numbers:
    print (n)