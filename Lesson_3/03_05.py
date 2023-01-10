# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи

# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5

def fibonacci_numbers(count: int):
    a, b = 1, 1
    list_numbers = [0]

    for i in range(count):
        list_numbers.append(a)
        list_numbers.insert (0,  a * (-1) ** i)
        a, b = b, b + a
    return list_numbers


numb = int(input("Введите число: "))
if numb <= 0:
    print("Введите число больше 0!")
else:
    all_list = fibonacci_numbers(numb)
    print(all_list)