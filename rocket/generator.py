import random

n = int(input())
print(n)

for _ in range(n):
    x = random.randint(-25000, 25000)
    y = random.randint(-25000, 25000)
    print(str(x) + " " + str(y))
