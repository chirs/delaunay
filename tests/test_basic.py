#!/usr/bin/env python3

import math

import pytest

from geometry.primitives import Point, Segment, Circle, Triangle
from geometry.convex import left_turn

p_null = Point.null()
p_unit = Point.unit() # (1, 0, 0)

p1 = Point(1, 0, 0)
p2 = Point(0, 1, 0)
p3 = Point(-1, 0, 0)
p4 = Point(0, -1, 0)

p5 = Point(1, 1, 0)


class TestPoint(object):

    def test_sanity(self):
        assert p_null == Point(0, 0, 0)
        assert p_unit == Point(1, 0, 0)

    def test_floating_point(self):
        # Break this. 
        
        assert Point(.5, 0, 0) == Point(.5, 0, 0)
        assert Point(.5, 0, 0) == Point(.25, 0, 0) + Point(.25, 0, 0)

    def test_angles(self):

        # These are literally all special cases now.
        assert p1.angle() == 0.0
        assert p2.angle() == math.pi / 2
        assert p3.angle() == math.pi
        assert p4.angle() == 3 * math.pi / 2

        assert p5.angle() == p5.normalize().angle() == math.pi / 4
                    


        
SEGMENT_INTERSECTIONS = [
    # Non-parallel, non-intersecting
    (Segment(Point(0, 0, 0), Point(5, 5, 0)), Segment(Point(0, 4, 0), Point(3, 4, 0)), False),
    # Parallel, non-intersecting
    (Segment(Point(0, 0, 0), Point(5, 0, 0)), Segment(Point(0, 2, 0), Point(5, 2, 0)), False),
    # Non-parallel, intersecting
    (Segment(Point(0, 0, 0), Point(5, 5, 0)), Segment(Point(0, 5, 0), Point(5, 0, 0)), True)
]


class TestSegment(object):

    @pytest.mark.parametrize("s1,s2,expected_intersect", SEGMENT_INTERSECTIONS)
    def test_segment_intersection(self, s1, s2, expected_intersect):
        assert s1.intersects(s2) == expected_intersect
        assert s2.intersects(s1) == expected_intersect



t1 = Triangle(
    Point(1, 0, 0),
    Point(0, 1, 0),
    Point(0, 0, 0)
    )


t2 = Triangle(
    Point(5, 8, 0),
    Point(-5, -5, 0),
    Point(-8, 3, 0),
    )

class TestTriangle(object):

    def test_circumcenter(self):
        assert t1.circumcenter() == Point(.5, .5, 0) # because it circumscribes a circle

    def test_radius(self):
        assert t1.circumcircle().radius == math.sqrt(2) / 2

    def test_ordering(self):
        t2n = t2.normalize()
        assert t2n.p1 == t2.p1
        assert t2n.p2 == t2.p3
        assert t2n.p3 == t2.p2





class TestLeftTurn(object):

    def test_left_turn(self):
        l1 = Point.null()
        l2 = Point.unit()
        l3 = Point(1, 1, 0)
        l4 = Point(1, -1, 0)
        
        assert left_turn(l1, l2, l3) == True
        assert left_turn(l1, l2, l4) == False

        p0 = Point.null()
        p1 = Point(0, 1, 0)

        assert left_turn(p0, p1, Point(-1, 1, 0)) == True
        assert left_turn(p0, p1, Point(-1, 0, 0)) == True

        assert left_turn(p0, p1, Point(1, 0, 0)) == False
        assert left_turn(p0, p1, Point(1, 1000, 0)) == False

