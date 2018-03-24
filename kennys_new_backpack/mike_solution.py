n = int(input())
 
ans = ""
 
while n > 1:
    if n % 3 == 0:
        ans += 'M'
        n //= 3
    elif n % 3 == 1:
        ans += 'R'
        n = (n - 1) // 3
    elif n % 3 == 2:
        ans += 'L'
        n = (n + 1) // 3
    else:
        print(n)
for step  in reversed(ans):
    print(step, end = '')
print()
 
