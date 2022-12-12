import random


def write_test(string, title):
    with open(f"{title}.txt", 'w') as f:
        f.write(string)
        f.close()


for i in range(30):
    n = random.randint(1, 30)

    write_test(f"{n}", str(i))
