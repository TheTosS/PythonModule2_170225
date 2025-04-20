## "Песочные часы символами"
rows = int(input("rows : "))


def one(i):
    for i in range(rows):
        if 2 <= rows <= 15:
            stars = (rows - i) * 2 - 1
            spaces = i
            print(" " * spaces + "*" * stars)


def two(j):
    for j in range(rows - 2, -1, -1):

        if 2 <= rows <= 15:
            stars = (rows - j) * 2 - 1
            spaces = j
            print(" " * spaces + "*" * stars)


one(1), two(1)
