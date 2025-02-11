from functools import cmp_to_key

def orientation(p, q, r):
    return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

def convex_hull(points):
    points.sort()
    hull = []
    
    for point in points:
        while len(hull) >= 2 and orientation(hull[-2], hull[-1], point) <= 0:
            hull.pop()
        hull.append(point)

    return hull

points = [(0, 0), (1, 1), (2, 2), (2, 0)]
print(convex_hull(points))  # Output: Convex Hull Points
