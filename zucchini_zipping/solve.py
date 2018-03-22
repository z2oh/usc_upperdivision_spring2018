t = int(input())
for _ in t:
    n = int(input())
    heights = list(map(int, input().split(" ")))
    expect_next = [False] * (n + 2)

    count = 0
    for h in heights:
        if not expect_next[h]:
            count += 1
        expect_next[h + 1] = True

    log = 0 
    while 1 << log < count:
        log += 1

    print(log)
