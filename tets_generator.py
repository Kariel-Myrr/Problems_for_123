from random import choice
from string import ascii_uppercase
import random

task = "A"
challenge = "hard"
lesson = "8"

level = "A"
trim = "1"
folder = f"level_{level}//trimester_{trim}//lesson_{lesson}//{challenge}//tests//"


def write_test(string, title):
    with open(f"{folder}/{lesson}_{task}/{str(title)}.txt", 'w') as f:
        # print(f"test {i} genrated to tests/{task}/{i}.txt")
        f.write(string)
        f.close()


for i in range(20):

    n = random.randint(1, 100)
    a = []
    for _ in range(n):
        a.append(str(random.randint(-100, 3)))

    s = ' '.join(a) + "\n"

    write_test(s, str(i))


n = random.randint(1, 100_000)
a = []
for _ in range(n):
    a.append(str(random.randint(-100_000, 100)))

s = ' '.join(a) + "\n"

write_test(s, "big")
