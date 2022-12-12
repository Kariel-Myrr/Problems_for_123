import random


def write_test(string, title):
    with open(f"{title}.txt", 'w') as f:
        f.write(string)
        f.close()


for i in range(30):
    a = random.randint(-100, 20)
    n = random.randint(1, 70)

    write_test(f"{a}\n{a+n}", str(i))
