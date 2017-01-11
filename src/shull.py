#!/usr/bin/env python3

"""
Computer delaunay triangulations of a randomly generated list of triangles

Using the s-hull algorithm described here:
http://www.s-hull.org/paper/s_hull.pdf


'Steven Fortune’s sweep-line algorithm is acknowledged as the inspiration
for the sweep-hull algorithm given here. The author would like
to acknowledge material support form RedGate.com a genuinely enlightened
company.'

"""


# http://www.qhull.org/html/index.htm
# http://www.cs.mcgill.ca/~fukuda/soft/polyfaq/polyfaq.html


import math
import random


"""
4. find the point xk that creates the smallest circum-circle with x0 and xj
and record the center of the circum-circle C.

5. order points [x0, xj, xk] to give a right handed system: this is the initial
seed convex hull.

6. resort the remaining points according to |xi − C|**2 to give points si

7. sequentially add the points si to the porpagating 2D convex hull that is
seeded with the triangle formed from [x0, xj, xk]. as a new point is added the facets of the 
2D-hull that are visible to it form new triangles.

8. a non-overlapping triangulation of the set of points is created. 
(This is an extremely fast method for creating an non-overlapping triangualtion of a 2D point set).

9. adjacent pairs of triangles of this triangulation must be ’flipped’ to 
create a Delaunay triangulation from the initial non-overlapping triangulation.
"""

def point_distance(p1, p2):
    distances = [v0 - v1 for (v0, v1) in zip(p1, p2)]
    return math.sqrt(sum([d**2 for d in distances]))


def generate_point():
    return [math.floor(100 * random.random()) for e in range(2)]


def generate_points():
    return [generate_point() for e in range(100)]


def average_points(points):
    sums = [sum(e) for e in zip(*points)]
    count = len(points)
    average = [e / float(count) for e in sums]
    return average


def closest_point(p, points):
    """
    Find closest point
    """

    min_distance = None
    closest_point = None

    for point in points:
        d = point_distance(p, point)
        if min_distance is None or d < min_distance:
            closest_point = point

    return point
            
    


def shull():
    """
    """

    points = generate_points()
    center = average_points(points)
    sorted = sorted(points, key=lambda p: point_distance(p, center))

    seed = closest_point(center, points)
    points.remove(seed)
    p2 = closest_point(seed, points)
    points.remove(p2)

    p3 = find_smallest_circumcircle(seed, p2, points)
    pa, pb, pc = order_right_handed(seed, p2, p3)
    
    

    for point in points:
        cc = create_circumcircle(seed, p2, point)
        



    


if __name__ == "__main__":
    #print(point_distance((0, 1, 2), (0, 3, 5)))
                        
    #print(generate_points())
    print(shull())
