from math import ceil

BASE = 3
DIRECTIONS = []

def main():
#input must be big enough, use python
    n = int(input())

#finding level in tree
    sum =  level = 1
    while(n > sum):
        sum += BASE ** level
        level += 1

#finding index in level
    index = n - (sum - BASE ** (level - 1))

#adding characters
    while(level > 1):
        add_direction(index % BASE)
        #index = ceil(index / BASE)#this is what breaks at 2^40 MUST have //
        level -= 1

#printing
    for step  in reversed(DIRECTIONS):
        print(step, end = '')
    print()

#adds characters to list
def add_direction(direct):
    if direct == 0:
        DIRECTIONS.append('R')
    elif direct == 1:
        DIRECTIONS.append('L')
    else:#2
        DIRECTIONS.append('M')

main()
