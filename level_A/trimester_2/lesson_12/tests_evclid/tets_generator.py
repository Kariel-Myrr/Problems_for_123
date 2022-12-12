import random


def write_test(string, title):
    with open(f"{title}.txt", 'w') as f:
        f.write(string)
        f.close()


for i in range(30):
    a = random.randint(1, 100_00)
    b = random.randint(1, 100_00)
    nod = random.randint(1, 100)

    write_test(f"{a * nod}\n{b * nod}", str(i))

a = random.randint(1, 100_0000)
b = random.randint(1, 100_0000)
nod = random.randint(1, 100)

write_test(f"{a * nod}\n{b * nod}", "big")
