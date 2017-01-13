from basic import Point, Segment, Circle, Triangle
import pytest


SEGMENT_INTERSECTIONS = [
    # Non-parallel, non-intersecting
    (Segment(Point(0, 0), Point(5, 5)), Segment(Point(0, 4), Point(3, 4)), False),
    # Parallel, non-intersecting
    (Segment(Point(0, 0), Point(5, 0)), Segment(Point(0, 2), Point(5, 2)), False),
    # Non-parallel, intersecting
    (Segment(Point(0, 0), Point(5, 5)), Segment(Point(0, 5), Point(5, 0)), True)
]


class TestSegment(object):
    @pytest.mark.parametrize(
        "s1,s2,expected_intersect",
        SEGMENT_INTERSECTIONS
    )
    def test_segment_intersection(self, s1, s2, expected_intersect):
        assert s1.intersects(s2) == expected_intersect
        assert s2.intersects(s1) == expected_intersect
