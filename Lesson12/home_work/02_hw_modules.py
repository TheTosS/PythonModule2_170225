# "Моделирование случайного леса"
# Создайте функцию, которая генерирует случайный "лес" в виде двумерного массива.
# Каждая ячейка массива должна представлять собой либо "дерево", либо "пустое пространство".
# Используйте random.random() для определения, будет ли в ячейке дерево или нет.
# Визуализируйте сгенерированный лес, например, выводя символы "T" для деревьев и "." для пустых пространств.
import random

# Пример результата:
forest = [['.', 'T', '.', '.', 'T', '.', '.', 'T', '.', '.'],
          ['T', '.', '.', 'T', '.', '.', '.', '.', 'T', '.'],
          ['.', '.', 'T', '.', '.', 'T', '.', '.', '.', 'T'],
          ['.', 'T', '.', '.', '.', '.', 'T', '.', '.', '.'],
          ['T', '.', '.', 'T', '.', 'T', '.', '.', 'T', '.'],
          ['.', '.', 'T', '.', '.', '.', '.', 'T', '.', '.'],
          ['T', '.', '.', '.', 'T', '.', '.', '.', '.', 'T'],
          ['.', 'T', '.', 'T', '.', '.', 'T', '.', '.', '.'],
          ['T', '.', '.', '.', '.', 'T', '.', 'T', '.', '.'],
          ['.', '.', 'T', '.', 'T', '.', '.', '.', 'T', '.']]
<<<<<<< HEAD
for line in forest:
    print(''.join(line))

import random


def generate_forest(rows, columns: int) -> list:
    new_forest = []
    for row in range(rows):
        line = [random.choice(["T", "."]) for row in range(columns)]
        new_forest.append(line)

    return new_forest
=======

def generate_forest(rows: int, columns: int) -> list:
    new_forest = []
    for i in range(rows):
        line = [random.choice([".", "T"]) for i in range(columns)]
        new_forest.append(line)
    return new_forest


forest = generate_forest(8, 8)
for line in forest:
    print(" ".join(line))
>>>>>>> 4f7cf1bf3d2dc2459cdaff08dc9316c53615f96f
