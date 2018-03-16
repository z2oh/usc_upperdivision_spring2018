import random

coll = ['r', 'b', 'g']

(x, y, z) = list(map(lambda x: x + 1, map(int, input().split(' '))))

xs = [''] * x
for i in range(x):
    xs[i] = random.choice(coll)
print(''.join(xs))

ys = [''] * y
for i in range(y):
    ys[i] = random.choice(coll)
print(''.join(ys))

zs = [''] * z
for i in range(z):
    zs[i] = random.choice(coll)
print(''.join(zs))
