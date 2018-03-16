from enum import Enum

# We grab our three lines of input and split them by character.
line1 = list(input())
line2 = list(input())
line3 = list(input())

class Entry:
    # By default, an entry has no set direction and a value of 0.
    def __init__(self):
        self.direction = Direction.UNSET
        self.val = 0 

# The direction scheme here points to an adjacent entry in the table.
# For example, XZ implies the direction back one x coordinate and back one
# z coordinate.
class Direction(Enum):
    X     = 0
    Y     = 1
    Z     = 2
    XY    = 3
    XZ    = 4
    YZ    = 5
    XYZ   = 6
    UNSET = 7

# Our table will have x_max * y_max * z_max entries in it.
x_max = len(line3)
y_max = len(line2)
z_max = len(line1)

# We build our table and fill it with empty entries (value = 0 and direction UNSET)
table = []
for i in range(x_max + 1):
    a = []
    for _ in range(y_max + 1):
        b = []
        for _ in range(z_max + 1):
            b.append(Entry())
        a.append(b)
    table.append(a)

# We construct our table used in memoization by iterating over every entry.
for x in range(1, x_max + 1):
    for y in range(1, y_max + 1):
        for z in range(1, z_max + 1):
            # If we have a match on the x,y, and z coordinates then we increment
            # the value for that table entry and set the dirextion to point to
            # the previous value.
            if line3[x-1] == line2[y-1] and line2[y-1] == line1[z-1]:
                table[x][y][z].val = table[x-1][y-1][z-1].val + 1
                table[x][y][z].direction = Direction.XYZ
            else:
                # Otherwise, we find the highest value neighbor, copy its value,
                # and point to it.
                max_ind, max_val = max(enumerate([
                    table[x-1][y][z].val,
                    table[x][y-1][z].val,
                    table[x][y][z-1].val,
                    table[x-1][y-1][z].val,
                    table[x-1][y][z-1].val,
                    table[x][y-1][z-1].val,
                    ]), key=lambda p: p[1])
                table[x][y][z].val = max_val
                table[x][y][z].direction = Direction(max_ind)

longest = []

print(table[x_max][y_max][z_max].val)

# Now that our table is filled out, we can trace back from the last entry and
# reconstruct a longest subsequence. The commented code below prints out a
# longest possible subsequence.
# current_x = x_max
# current_y = y_max
# current_z = z_max
# while table[current_x][current_y][current_z].val is not 0:
    # current_direction = table[current_x][current_y][current_z].direction
    # if current_direction == Direction.XYZ:
        # longest.append(line3[current_x - 1])
        # current_x = current_x - 1
        # current_y = current_y - 1
        # current_z = current_z - 1
    # elif current_direction == Direction.X:
        # current_x = current_x - 1
    # elif current_direction == Direction.Y:
        # current_y = current_y - 1
    # elif current_direction == Direction.Z:
        # current_z = current_z - 1
    # elif current_direction == Direction.XY:
        # current_x = current_x - 1
        # current_y = current_y - 1
    # elif current_direction == Direction.XZ:
        # current_x = current_x - 1
        # current_z = current_z - 1
    # elif current_direction == Direction.YZ:
        # current_y = current_y - 1
        # current_z = current_z - 1
# 
# longest.reverse()
# print(''.join(longest))
