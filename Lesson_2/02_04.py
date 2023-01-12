# Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

num = int(input("Введите число N: "))
num1 = int(input("Позиция 1: "))
num2 = int(input("Позиция 2: "))

nums_list = list(range(-num, num + 1))

print(nums_list)
len_list = len(nums_list)

if len_list >= num1 > 0 and len_list >= num2 > 0:
    print(nums_list[num1 - 1] * nums_list[num2 - 1])
else:
    print("Индекс выходит за границы!")