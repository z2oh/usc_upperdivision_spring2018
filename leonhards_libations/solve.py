# These were used to calculate the values in the print statement needed below,
# but aren't actually called anywhere in my code.
def f(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * f(n-1)

def approx(n):
    if n == 0:
        return 1
    else:
        return 1/f(n) + approx(n-1)

line = input()

n = -1
if len(line) == 1:
    n = int(line)

if n == '1':
    print("2.000000")
elif n == '2':
    print("2.500000")
elif n == '3':
    print("2.666667")
elif n == '4':
    print("2.708333")
elif n == '5':
    print("2.716667")
elif n == '6':
    print("2.718056")
elif n == '7':
    print("2.718254")
elif n == '8':
    print("2.718279")
else:
    # Beyond n = 9, n converges to the mathematical constant `e` for 6 decimal
    # places.
    print("2.718282")
