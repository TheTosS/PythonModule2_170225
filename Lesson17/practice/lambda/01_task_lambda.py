# Дан готовый код
# def is_even(n):
#    return n % 2 == 0


numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# even_numbers = list(filter(is_even, numbers))
print(even_numbers)

# Задача: перепишите код, используя lambda-функцию
