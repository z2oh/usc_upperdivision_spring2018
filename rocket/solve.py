import math

n = int(input())
points = [[0, 0, 0]] * n

for i in range(n):
    points[i] = list(map(float, input().split(' '))) + [0]

# Sort by x and then y
points.sort(key=lambda x: x[0])
points.sort(key=lambda x: x[1])

# Remove the first point, which is the lowest leftmost points. This point is
# part of our convex hull.
p0 = points[0]
points = points[1:]

# Now we determine the polar coordinates of each point relative to p0
# We don't actually have to compute the angle here, but this is still O(n)
# so we won't worry about it for now.
for point in points:
    point[2] = math.atan2(point[1] - p0[1], point[0] - p0[0])

# We sort by the polar angles to make a stack of increasing polar coordinates
# relative to p0
points.sort(key = lambda x: x[2])

# We perform Graham's scan on the points to determine the convex hull.
stack = [p0, points[0], points[1]]
for i in range(2, n-1):
    p3 = points[i]
    cross = -1
    while cross < 0:
        p1 = stack[-2]
        p2 = stack[-1]
        # This quickly calculates the cross product between p1p2 and p1p3.
        # If `cross` is 0, the points are colinear. If `cross` is positive we
        # have made a left turn and can move on to the next point. If `cross` is
        # negative, we have made a right turn and pop the top point and
        # continue.
        cross = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
        if cross < 0:
            stack.pop()
    stack.append(points[i])

# Now `stack` contains the points of our convex hull in counterclockwise order.
# We can now calculate the area of the polygon.
# This is the de-facto way of computing area for a 2D convex polygon, and is
# an application of Green's theorem.
area = 0
for i in range(1, len(stack)):
    area += stack[i-1][0]*stack[i][1] - stack[i][0]*stack[i-1][1]
# Account for the wrapping from the last point to the first...
area += stack[0][0]*stack[-1][1] - stack[-1][0]*stack[0][1]
area = area / 2

print(area)
