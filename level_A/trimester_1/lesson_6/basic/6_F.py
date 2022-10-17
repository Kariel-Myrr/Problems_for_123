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

# in : c - str
# out : none
# берет строку и печатает ее в рамочке
def my_print(c):
    print("=" * (len(c) + 4))
    print("| " + c + " |")
    print("=" * (len(c) + 4))


a = my_input()
b = my_input()

sum_ = str(a + b)

my_print(sum_)
