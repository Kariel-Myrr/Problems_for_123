# Считать два числа в рамочке, вывести их сумму


# in : none
# out : int
# считывает из ввода число обрамленное в рамочку
def my_input():
    buff = input()

    symbol = input().split(" ")
    symbol = int(symbol[1])

    buff = input()

    return symbol


a = my_input()
b = my_input()

print(a+b)
