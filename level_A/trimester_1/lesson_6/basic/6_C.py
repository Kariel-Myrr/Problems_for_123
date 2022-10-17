
# Выводим две строки в рамочке, а потом их сумму в другой рамке


# in : c - str
# out : none
# берет строку и печатает ее в рамочке
def my_print(c):
    print("="*(len(c) + 4))
    print("| " + c + " |")
    print("="*(len(c) + 4))


a = input()
b = input()
c = input()
d = input()

sum_ = a + b

my_print(a)
my_print(b)
my_print(c)
my_print(d)
