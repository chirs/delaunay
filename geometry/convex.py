
from primitives import Point, Segment, Graph, Circle


def values_over_grayscale_spectrum(n):
    
    return [e for e in range(0, 255, int(255 / n))]




def graham_scan(points):
    """
    Only left turns are acceptable.
    All right turns will be eliminated.
    """


    points_ = sorted(points, key=lambda p: p.y) # the bottom-most point
    start = points_[0]

    # sort by angle from unit circle.
    # So that there is a clean sweep of points, I think.
    sorted_points = sorted(points_[1:], key=lambda p: (p - start).angle())

    visited = [start, sorted_points[0]]
    unvisited = sorted_points[1:]

    candidate = unvisited.pop(0)

    turns_left = left_turn(visited[-2], visited[-1], candidate)

    while unvisited:
        
        turns_left = left_turn(visited[-2], visited[-1], candidate)

        if turns_left:
            visited.append(candidate)
            candidate = unvisited.pop(0)
            # final candidate getting forgotten when while loop terminates
        else:
            # turns right; ignore collinearity
            visited.pop()

    visited.append(start)
    
    edges = [Segment(start, end) for (start, end) in zip(visited, visited[1:])]
    graph = Graph(edges)

    [p.draw() for p in points]
    graph.draw()

            

def left_turn(p1, p2, p3):
    # Not confident this is correct.
    # Could use some TESTING


    s1 = Segment(p1, p2)
    v1 = s1.vector().normalize()

    s2 = Segment(p2, p3)
    v2 = s2.vector().normalize()

    cross_product = v1.cross_product(v2)

    if cross_product > 0:
        return True

    elif cross_product < 0:
        return False

    else:
        raise # Collinear, right?



def main():

    scale = 10
    points = [Point.random(scale) for e in range(100)]

    graham_scan(points)


if __name__ == "__main__":
    main()
