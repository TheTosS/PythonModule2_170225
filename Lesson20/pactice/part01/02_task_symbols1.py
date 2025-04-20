side = int(input("side :"))

if 2 <= side <= 15:
    for i in range(side):
        print(" " * (side - i - 1) + "+" + " " * (i * 2) + "+")
    for i in range(side - 2, -1, -1):
        print(" " * (side - i - 1) + "+" + " " * (i * 2) + "+")



else:
    print("side должна быть от 3 до 14.")
