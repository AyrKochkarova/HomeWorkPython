# Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

from random import uniform


def list_random_numbers(count: int):
    list_numbers = []
    
    for i in range(count):
        list_numbers.append(round(uniform(1, count), 2))
    return list_numbers


def dif_max_min(list_numbers: list):
    num_max = num_min = round(list_numbers[0] % 1, 2)

    for k in range(1, len(list_numbers)):
        num = round(list_numbers[k] % 1, 2)
        if num > num_max:
            num_max = num
        elif num < num_min:
            num_min = num

    result = round(num_max - num_min, 2)
    print(f"Min: {num_min}, Max: {num_max}. Difference: {result}")
    return result


numb = int(input("Введите количество чисел: "))
if numb <= 0:
    print("Введите число больше 0!")
else:
    all_list = list_random_numbers(numb)
    print(all_list)
    dif_max_min(all_list)