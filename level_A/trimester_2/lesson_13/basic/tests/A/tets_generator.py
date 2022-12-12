import random


def write_test(string, title):
    with open(f"{title}.txt", 'w') as f:
        f.write(string)
        f.close()


for i in range(30):
    a = random.randint(1, 100)
    n = random.randint(0, 100)

    write_test(f"{a}\n{n}", str(i))
