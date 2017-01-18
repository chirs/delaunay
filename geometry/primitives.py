#!/usr/bin/env python3

import math
import random

from collections import defaultdict



radians2degrees = lambda r: 180 * radians / math.pi
degrees2radians = lambda d: degrees * math.pi / 180


def random_points(n, scale=1, grid=False):
    """
    Generate random points
    """

    xs = [scale * random.random() for e in range(n)]
    if grid:
        xs = [round(x) for x in xs]

    ys = [scale * random.random() for e in range(n)]
    if grid:
        ys = [round(y) for y in ys]

    zs = [scale * 0 for e in range(n)]

    return [Point(*p) for p in zip(xs, ys, zs)]



class Point(object):
    """
    A point
    """
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    def __hash__(self):
        t = (self.x, self.y)
        return hash(t)

    def __add__(self, p2):
        x = self.x + p2.x
        y = self.y + p2.y
        z = self.z + p2.z
        return Point(x, y, z)

    def __sub__(self, p2):
        x = self.x - p2.x
        y = self.y - p2.y
        z = self.z - p2.z
        return Point(x, y, z)


    def __eq__(self, p2):
        return self.x == p2.x and self.y == p2.y and self.z == p2.z

        
    def __gt__(self, p2):
        # Enough for comparison with __eq__?
        if self.x != p2.x:
            return self.x > p2.x
        
        else:
            return self.y > p2.y



    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)



    def normalize(self):
        magnitude = self.magnitude()
        return Point(self.x / magnitude, 
                     self.y / magnitude,
                     self.z / magnitude)


    def angle(self):
        """in radians"""
        # Is this correct angle? 
        p_ = self.normalize()

        try:
            return math.asin(self.x)
        except:
            import pdb; pdb.set_trace()
            x = 5

    def distance(self, p2):
        d_squared = (self.x - p2.x)**2 + (self.y - p2.y)**2 + (self.z - p2.z)**2
        return math.sqrt(d_squared)

    def draw(self):
        import rhinoscriptsyntax as rs
        rs.AddPoint([self.x, self.y, self.z])
        #ellipse(mouseX, mouseY, 20, 20)


    def cross_product(self, p2):
        # Add z value to this?
        return (self.x * p2.y) - (self.y * p2.x)

    def tuple(self):
        return (self.x, self.y, self.z)


    @staticmethod
    def unit():
        return Point(1, 0, 0)

    @staticmethod
    def null():
        return Point(0, 0, 0)


    @staticmethod
    def random(scale, grid=False):

        x = scale * random.random()
        if grid:
            x = round(x)

        y = scale * random.random()
        if grid:
            y = round(y)

        z = 0

        return Point(x, y, z)



def points_average(points):
    """
    Take the average of a list of points.
    """
    xs = sum([p.x for p in points])
    ys = sum([p.y for p in points])
    count = float(len(points))
    average = Point(xs/count, ys/count, 0)
    return average


class Segment(object):
    """
    A line segment
    """
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return "Segment {}, {}".format(self.p1, self.p2)

    # Some definite issues to think about here wrt directionality of segments.

    def __gt__(self, s2):
        # Check if they're the same?
        if self.p1 != s2.p1:
            return self.p1 < s2.p1 
        else:
            return self.p2 < s2.p2

    def __eq__(self, s2):
        if self.p1 == s2.p1 and self.p2 == s2.p2:
            return True
        elif self.p2 == s2.p1 and self.p1 == s2.p2:
            return True
        else:
            return False

    def __hash__(self):
        t = (self.p1.x, self.p1.y, self.p2.x, self.p2.x)
        return hash(t)

    def reverse(self):
        return Segment(self.p2, self.p1)

    def length(self):
        return self.vector().magnitude()

    def tuple(self):
        return (self.p1.tuple(), self.p2.tuple())

    def move(self, vector):
        return Segment(self.p1+vector, self.p2+vector)

    def vector(self):
        return self.p2 - self.p1

    def intersects(self, s2):
        p = self.p1
        q = s2.p1
        r = self.vector()
        s = s2.vector()

        r_cross_s = r.cross_product(s)

        if r_cross_s == 0:
            return False   # todo: fix case of two collinear, overlapping segments

        t = (q - p).cross_product(s) / r_cross_s
        u = (q - p).cross_product(r) / r_cross_s
        return (0 < t < 1) and (0 < u < 1)

    def draw(self):
        import rhinoscriptsyntax as rs
        rs.AddLine([self.p1.x, self.p1.y, 0], [self.p2.x, self.p2.y, 0])


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


    def draw(self):
        import rhinoscriptsyntax as rs
        rs.AddCircle([self.center.x, self.center.y, 0], self.radius)
        

    def cartesian_to_polar(self, p): pass
    def polar_to_cartesian(theta): pass


class Triangle(object):
    """
    A triangle is a polygon with three edges and three vertices. 
    It is one of the basic shapes in geometry.
    """
    
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3


    def points(self):
        return [self.p1, self.p2, self.p3]

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

        cc = Point(x,y, 0) + self.p1

        return cc
        
    def circumcircle(self):
        center = self.circumcenter()
        radius = center.distance(self.p1)
        return Circle(center, radius)


    def draw(self):
        import rhinoscriptsyntax as rs
        l = [e.tuple() for e in self.points()]
        l.append(l[0])
        rs.AddPolyline(l)


    def reorder(self):
        pass


class Graph(object): 
    """
    a graph is vertices and edges
    """

    def __init__(self, edges=None):
        if edges is None:
            edges = []

        self.edges = set(edges)

    def vertices(self):
        s = set()
        for edge in self.edges:
            s.add(edge.p1)
            s.add(edge.p2)

        return s


    def swap_edges(self, l1, l2):
        pass


    def add_edge(self, edge):
        self.edges.add(edge)

    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge)

    def add_triangle(self, triangle):
        self.add_edges(triangle.segments())

    def intersects_edge(self, segment):
        for edge in self.edges:
            if segment.intersects(edge):
                return True

        return False


    def adjacency_map(self):
        d = defaultdict(list)

        for edge in self.edges:
            #if edge.p1 not in d: d[edge.p1] = []
            #if edge.p2 not in d: d[edge.p2] = []

            #d[edge.p1].append(d[edge.p2]) # Vicious circle! 

            d[edge.p1].append(edge.p2)
            d[edge.p2].append(edge.p1)

        return d


    def triangles(self):
        triangles = set()
        adjacency_map = self.adjacency_map()

        for p1, p2s in adjacency_map.items():

            for p2 in p2s:
                p2_neighbors = adjacency_map[p2]

                for p3 in p2_neighbors:
                    if p3 != p1 and p1 in adjacency_map[p3]:
                        triangles.add(tuple(sorted([p1,p2,p3])))

        return triangles


    def cycles(self, depth=2):
        pass

    def draw(self):
        for edge in self.edges:
            edge.draw()

    

class Triangulation(object): 
    """
    division of the Euclidean plane into triangles and of Euclidean spaces into simplices
    """

    def __init__(self, triangles=None):
        if triangles is None:
            triangles = []

        self.triangles = triangles

    def adjacents(self):
        d = defaultdict(int)

        for triangle in self.triangles:
            segments = triangle.segments()
            for segment in segments:
                d[segment] += 1
                d[segment.reverse()] += 1

        multiples = [k for (k, v) in d.items() if v > 1]

        s = set()
        for m in multiples:
            r = m.reverse()
            if m < r:
                s.add(m)
            else:
                s.add(r)

        return s
            
            

    def add_triangle(self, triangle):
        self.triangles.append(triangle)

    def points(self):
        s = set()
        for triangle in self.triangles:
            s.add(triangle.p1)
            s.add(triangle.p2)
            s.add(triangle.p3)

        return s

    def segments(self):
        s = set()

        for triangle in self.triangles:
            for segment in triangle.segments():
                s.add(segment)


    def draw(self):
                        
        pass




class Path(object): pass    
class Mesh(object): pass
class Voronoi(object): pass
class ConvexHull(object): pass



def test():
    pass


if __name__ == "__main__":
    test()
