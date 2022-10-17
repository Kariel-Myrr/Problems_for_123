# Прочитать N чисел в рамочках и найти их минимум. Минимум вывести в рамочке

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


n = int(input())

min_ = -100000000

for i in range(n):
    a = my_input()
    if min_ > a:
        min_ = a

my_print(str(min_))
