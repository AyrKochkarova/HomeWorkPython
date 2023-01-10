# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.

# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

num = float(input())
length = len(str(num))
num = num * 10 **(length-2)

summ_numbers = 0 

while num:
    summ_numbers += num % 10
    num //= 10

print(int(summ_numbers))