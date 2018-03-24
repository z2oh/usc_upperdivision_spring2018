n = int(input())
directs=''
while n > 1:
    mod = n % 3;
    n = (n + 1) // 3
    if mod == 0:
        step = 'M'
    elif mod == 1:
        step = 'R'
    else:#2
        step = 'L'

    directs = step+ directs
print(directs)
