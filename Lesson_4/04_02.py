# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# in
# 54
# 
# out
# [2, 3, 3, 3]
# 
# in
# 9990
# 
# out
# [2, 3, 3, 3, 5, 37]
# 
# in
# 650
# 
# out
# [2, 5, 5, 13]

import math 


def prime_numbers(num): 
    list_numbers = []
    while num % 2 == 0: 
        list_numbers.append(2) 
        num = num / 2 
 
    for i in range(3, int(math.sqrt(num)) + 1, 2): 
 
        while num % i == 0: 
            list_numbers.append(i) 
            num = num / i
    if num > 2: 
        print(num) 
    print(list_numbers)
 
numb = int(input("Введите число: "))
prime_numbers(numb) 