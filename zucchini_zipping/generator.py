import random

T, n_min_exp, n_max_exp = list(map(int, input().split(" ")))
print(T)
for _ in range(T):
    n = random.randint(2**n_min_exp, 2**n_max_exp)
    print(n)
    li = list(map(lambda x: str(x + 1), list(range(n))))
    random.shuffle(li)
    print(" ".join(li))
