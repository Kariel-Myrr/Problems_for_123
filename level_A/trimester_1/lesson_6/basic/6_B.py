# Напишите функцию, которая выводит строку в рамочке



# in : c - str
# out : none
# берет строку и печатает ее в рамочке
def my_print(c):
    print("="*(len(c) + 4))
    print("| " + c + " |")
    print("="*(len(c) + 4))


a = input()
my_print(a)