# Элементы массива в своих рамочках

# in : c - str
# out : none
# берет строку и печатает ее в рамочке
def my_print(c):
    print("=" * (len(c) + 4))
    print("| " + c + " |")
    print("=" * (len(c) + 4))


[my_print(i) for i in input().split(" ")]
