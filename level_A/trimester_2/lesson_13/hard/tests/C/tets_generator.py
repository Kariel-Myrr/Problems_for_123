import random


def write_test(string, title):
    with open(f"{title}.txt", 'w') as f:
        f.write(string)
        f.close()


for i in range(30):
    n = random.randint(10, 40)
    s = ""
    for _ in range(n):
        s += str(random.randint(5, 100)) + "\n"
    s += "0\n"
    write_test(s, str(i))
