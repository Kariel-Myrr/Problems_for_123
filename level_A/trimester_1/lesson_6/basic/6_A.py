# Напишите функцию принта, которая выводит букву в рамочке


# in : c - str
# out : none
# берет строку и печатает ее в рамочке
def my_print(c):
    print("=====")
    print("| " + c + " |")
    print("=====")


a = input()
my_print(a)
