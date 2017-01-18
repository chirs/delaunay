#!/usr/bin/env python3

"""
Delaunay triangulation algorithm(s)
"""

from primitives import Point, Segment, Triangle, Graph, Triangulation

    
    
def shull():
    """
    presumably the s-hull implementation of delaunay triangulation
    """
    points = [Point.random(10) for e in range(100)]

    average_point = sum(points, Point.null()).divide(float(len(points)))

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
                s1.draw()

    triangles = [Triangle(*triangle) for triangle in g.triangles()]
    t  = Triangulation(triangles)


    
def main():
    """
    delaunay triangulation implementations
    """

    shull()
    delaunay()


    
if __name__ == "__main__":
    main()
