# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# number = input("Введите число: ").replace('.', '')
# sum = 0
# for i in range(len(number)):
#     sum += int(number[i])
# print (sum)


# Напишите программу, которая принимает на вход число 
# N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# number = int(input("Введите число: "))
# list = [1]
# i = 2
# while i <= number:
#     list.append(list[i - 2] * i)
#     i += 1
# print (list)


# Задайте список из n чисел последовательности
#  $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# number = int (input('Введите число: '))
# if number != 0:
#     list = []
#     sum = 0
#     for i in range(1, number+1):
#         list.append(round((1+1/i)**i, 2))
#     print(*list, sep=', ')
#     for i in range(1, number+1):
#         result = round((1+1/i)**i, 2)
#         sum += result
#     print(f"Сумма членов последовательности =", sum)
# else:
#     print('Деление на 0!!!')