#!/usr/bin/env python3

"""
Computer delaunay triangulations of a randomly generated list of triangles

Using the s-hull algorithm described here:
http://www.s-hull.org/paper/s_hull.pdf

# http://www.qhull.org/html/index.htm
# http://www.cs.mcgill.ca/~fukuda/soft/polyfaq/polyfaq.html
"""


from primitives import Point, Segment, Triangle, Graph

### todo

# 1. Right-handed ordering of triangles. -> improve; 
# 2. Triangles / cycles from a graph
# 3. Triangle pairs from a triangulation

# 5. convex hull

#Constrained Delaunay triangulation
# https://en.wikipedia.org/wiki/Mesh_generation
# https://www.openmesh.org/


                                 
def main():
    """
    Generate connection images
    """

    delaunay()
    

def delaunay():
    """
    delaunay triangulation implementations
    """
    shull()
        
    
def shull():
    """
    presumably the s-hull implementation of delaunay triangulation
    """
    points = [Point(10) for e in range(100)]

    average_point = points_average(points) # Maybe just pick a point at random.
    sorted_points = sorted(points, key=lambda p: average_point.distance(p))
    seed_point = sorted_points[0]
    sorted_by_seed = sorted(sorted_points[1:], key=lambda p: seed_point.distance(p))
    p2 = sorted_by_seed[0]
    circumcircle_sorted = sorted(sorted_by_seed[1:], key=lambda p: Triangle(seed_point, p2, p).circumcircle().radius)
    p3 = circumcircle_sorted[0]
    triangle = Triangle(seed_point, p2, p3)

    circumcenter = triangle.circumcenter()
    points_from_circumcenter = sorted(circumcircle_sorted[1:], key=lambda p: circumcenter.distance(p))


    g = Graph()
    g.add_triangle(triangle)

    for p1 in points_from_circumcenter:
        added_points = g.vertices()
        for p2 in added_points:
            s1 = Segment(p1, p2)
            if not g.intersects_edge(s1):
                g.add_edge(s1)

    triangles = [Triangle(*triangle) for triangle in g.triangles()]
    t  = Triangulation(triangles)

    #t.draw()
    #g.draw()

    for a in t.adjacents():
        a.draw()

    #for edge in g.edges:
    #    edge.draw()




def incremental(points):
    unconnected = points

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
        



if __name__ == "__main__":
    main()
