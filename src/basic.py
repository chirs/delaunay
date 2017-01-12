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

### todo

# 2. Right-handed ordering of points on a circle.
# 3. check if two segments intersect. (http://stackoverflow.com/questions/563198/how-do-you-detect-where-two-line-segments-intersect)
# 4. The Euclidean minimum spanning tree of a set of points is a subset of the Delaunay triangulation of the same points, and this can be exploited to compute it efficiently.
# 5. convex hull



### Driving

# Constrained Delaunay triangulation

# https://en.wikipedia.org/wiki/Mesh_generation

# https://www.openmesh.org/



class Graph(object):
    pass






class Segment(object):

    """
    A line segment
    """

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    
    def __repr__(self):
        return "Segment {}, {}".format(self.p1, self.p2)


    def intersection(self, s2):
        """
        Return the point where Segment 1 and 2 intersect.
        """
        pass


    def draw(self):
        import rhinoscriptsyntax as rs
        rs.AddLine([self.p1.x, self.p1.y, 0], [self.p2.x, self.p2.y, 0])



class Intersection(object):

    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2




class Point(object):

    """
    A point
    """

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


    def __eq__(self, p2):
        return self.x == p2.x and self.y == p2.y
        

    def distance(self, p2):
        d_squared = (self.x - p2.x)**2 + (self.y - p2.y)**2
        return math.sqrt(d_squared)

    def draw(self):
        import rhinoscriptsyntax as rs
        rs.AddPoint([self.x, self.y, 0])



class Circle(object):
    """
    the set of all points in a plane that are at a given distance from a given point, the centre.
    """
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __repr__(self):
        return "Circle (c={}, r={})".format(self.center, self.radius)



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
    """
    A triangle is a polygon with three edges and three vertices. 
    It is one of the basic shapes in geometry.
    """
    
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3


    def segments(self):
        return [
            Segment(self.p1, self.p2),
            Segment(self.p2, self.p3),
            Segment(self.p3, self.p1),
            ]


    def circumcenter(self):
        """
        The center point of the circle that circumscribes three points.
        """
    
        b_ = self.p2 - self.p1
        c_ = self.p3 - self.p1
        D_ = 2 * (b_.x * c_.y - b_.y * c_.x)

        x = (c_.y * (b_.x**2 + b_.y**2) - b_.y * (c_.x**2 + c_.y**2)) / D_
        y = (b_.x * (c_.x ** 2 + c_.y ** 2) - c_.x * (b_.x **2 + b_.y**2)) / D_
        return Point(x, y)
        
    def circumcircle(self):
        center = self.circumcenter()
        radius = center.distance(self.p1)
        return Circle(center, radius)





def points_average(points):
    """
    Take the average of a list of points.
    """
    xs = sum([p.x for p in points])
    ys = sum([p.y for p in points])
    count = float(len(points))
    #average = Point([xs/count, ys/count]) 
    average = Point(0, 0)
    return average



def draw_all_lines(points):
    """
    Draw every line.
    """
    for start in points:
        for end in points:
            if start != end:
                line = Segment(start, end)
                line.draw()




def main():

    points = random_points(100, 10)
    center = points_average(points)

    #for point in points:
    #    point.draw()

    #p1 = Point(0, 10)
    #p2 = Point(10, 0)
    #s1 = Segment(p1, p2)
    #s1.draw()

    #connect_points(points)

    delaunay_algorithms()



def connect_points(points):
    npoints = points[:]
    random.shuffle(npoints)

    segments = [Segment(start, end) for (start, end) in zip(npoints, npoints[1:])]
    for s in segments:
        s.draw()



def delaunay_connect(points):

    npoints = points[:]
    random.shuffle(npoints)

    p1 = points[0]
    
    lines = []

    for p in points[1:]:
        # lines.append...
        pass # do something?
    
    #flip_triangles(lines)



def delaunay_algorithms():

    # https://en.wikipedia.org/wiki/Delaunay_triangulation#Algorithms

    #flip()
    for segment in incremental():
        segment.draw()
    #divide_and_conquer()
    #sweephull()

    pass

    

def incremental():
    unconnected = random_points(100, 10)
    [point.draw() for point in unconnected]
    connected = set()

    previous = unconnected.pop()
    p2 = unconnected.pop()

    segments = []
    
    while unconnected:
        unconnected = sorted(unconnected, key=lambda p: previous.distance(p))
        point = unconnected.pop(0)
        segment = Segment(previous, point)
        segments.append(segment)
        


        previous = point






    return segments
        
        

        
            

        
        
        
        

    
    

def random_points(n, scale=1):
    
    xs = [scale * random.random() for e in range(n)]
    ys = [scale * random.random() for e in range(n)]
    zs = [scale * 0 for e in range(n)]


    
    return [Point(*p) for p in zip(xs, ys)]
    
    

    


if __name__ == "__main__":
    #print(point_distance((0, 1, 2), (0, 3, 5)))
                        
    #print(generate_points())
    #print(shull())

    main()
