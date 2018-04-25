# Read in number of test cases.
t = int(input())

# For each test case.
for _ in range(t):
    # Read the number of zucchinis.
    n = int(input())

    # Grab the heights of each zucchini in a list.
    heights = list(map(int, input().split(" ")))

    # Build our other list and initialize to False. We use two extra indices
    # to avoid having to do bounds checking.
    expect_next = [False] * (n + 2)

    # We keep track of the number of sequences we have found in `count`.
    count = 0

    # For each zucchini, if we have not seen the previous zucchini 
    # (with height - 1) we increase our count by 1. We then set the value for
    # our next zucchini (with height + 1) to True, indicating we expect to see
    # it further along in the sequence.
    for h in heights:
        if not expect_next[h]:
            count += 1
        expect_next[h + 1] = True

    # We take the ceiling of the log_2 of count...
    log = 0 
    while 1 << log < count:
        log += 1

    # And print out our answer.
    print(log)
