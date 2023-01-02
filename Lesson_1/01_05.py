# Напишите программу, которая принимает на вход
# координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math
firstNumberX = int(input("Введите  X первой точки "))
firstNumberY = int(input("Введите  Y первой точки "))
secondNumberX = int(input("Введите  X второй точки "))
secondNumberY = int(input("Введите  Y второй точки "))
print("Расстояние в 2D пространстве равно : ", math.sqrt((firstNumberX-secondNumberX) * (firstNumberX-secondNumberX) +
      (firstNumberY-secondNumberY) * (firstNumberY-secondNumberY)))