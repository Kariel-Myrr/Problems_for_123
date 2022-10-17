
# Считать 4 числа в рамочке, вывести их минимум


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


def my_min_3(a, b, c):
    if a < b:
        if a < c:
            return a
        else:
            return c
    else:
        if b < c:
            return b
        else:
            return c


def my_min_4(a, b, c, d):
    if a < b:
        return my_min_3(a, c, d)
    else:
        return my_min_3(b, c, d)


a = my_input()
b = my_input()
c = my_input()
d = my_input()
my_print(str(my_min_4(a, b, c, d)))
