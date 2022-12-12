import random


def write_test(string, title):
    with open(f"{title}.txt", 'w') as f:
        f.write(string)
        f.close()


for i in range(30):
    n = random.randint(1, 30)
    x = random.randint(1, 5)

    write_test(f"{int(x * pow(2, n))}", str(i))
