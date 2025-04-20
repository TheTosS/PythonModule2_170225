height = int(input("Height: "))
if 2 <= height <= 15:
    for i in range(height):
        print(" " * (height - i - 1) + "/" + " " * (i * 2) + "\\")
    print("_" * (height * 2))
else:
    print("Высота должна быть от 2 до 15.")
