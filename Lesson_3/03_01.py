# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4
# out
# [4, 2, 4, 9]
# 8

from random import sample


def list_random_numbers(count: int) -> list:
    list_numbers = sample(range(1, count * 10), count)
    return list_numbers


def sum_odd_pos(list_numbers: list):
    sum_numbers = 0
    for k in range(0, len(list_numbers), 2):
        sum_numbers += list_numbers[k]
    return sum_numbers


numb = int(input("Введите количество чисел: "))
if numb < 0:
    print("Введите число больше 0!")
else:
    all_list = list_random_numbers(numb)
    print(all_list)
    print(sum_odd_pos(all_list))