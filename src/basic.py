#!/usr/bin/env python3

"""
Computer delaunay triangulations of a randomly generated list of triangles

Using the s-hull algorithm described here:
http://www.s-hull.org/paper/s_hull.pdf

# http://www.qhull.org/html/index.htm
# http://www.cs.mcgill.ca/~fukuda/soft/polyfaq/polyfaq.html
"""

import math
import random



class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    def __add__(self, p2):
        x = self.x + p2.x
        y = self.y + p2.y
        return Point(x, y)

    def __sub__(self, p2):
        x = self.x - p2.x
        y = self.y - p2.y
        return Point(x, y)
        

    def distance(self, p2):
        d_squared = (self.x - p2.x)**2 + (self.y - p2.y)**2
        return math.sqrt(d_squared)


class Circle(object):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


    def distance(self, point):
        return point.distance(self.center)

    def distance_from_edge(self, point):
        d = self.distance(point)

        if d > self.radius:
            return d - self.radius
        else:
            return self.radius - d
            

    def inside(self, point):
        return self.distance(point) < self.radius


    def cartesian_to_polar(self, p):
        pass

    def polar_to_cartesian(theta):
        pass



class Triangle(object):
    
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3


    def circumcircle(self):
        pass


"""
def point_distance(p1, p2):
    distances = [v0 - v1 for (v0, v1) in zip(p1, p2)]
    return math.sqrt(sum([d**2 for d in distances]))

"""





def inside_circle(p, circle):
    cp = circle.center



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
