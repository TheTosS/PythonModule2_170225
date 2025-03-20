# Задача: Дан список из n элементов, заполненный произвольными целыми числами.
# Найдите сумму всех положительных элементов.

# Решение:

numbers = [6, -4, 3, 8, 2, 0, 7]

summa = 0
for number in numbers:
    if number > 0:
        summa += number

print(summa)

# Оформите решение задачи в виде функции

def numbers_sum(numbers):
    summa = 0
    for number in numbers:
        if number > 0:
            summa += number

