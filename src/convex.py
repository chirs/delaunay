
from primitives import Point, Segment, Graph


def graham_scan(points):
    p1x = sorted(points, key=lambda p: p.x) # Sort by x coordinate

    start = p1x[0]

    p2x = sorted([p2 - start for p2 in p1x[1:]], key=lambda p: p.normalize().angle()) 
    # Sorting in order of angle does not require computing the angle. It is possible to use any function of the angle which is monotonic in the interval {\displaystyle [0,\pi ]} [0,\pi] 
    # The cosine is easily computed using the dot product, or the slope of the line may be used.

    candidate_stack = [start, p2x[0], p2x[1]]
    unvisited = p2x[2:]

    while unvisited:
        candidate_point = unvisited.pop(0)

        goes_left = left_turn(candidate_stack[-2], candidate_stack[-1], candidate_point)

        if goes_left:
            # remove this point and the previous point.
            candidate_stack.append(candidate_point)



        else:
            candidate_stack.pop()


    candidate_stack.append(start)
    edges = [Segment(start, end) for (start, end) in zip(candidate_stack, candidate_stack[1:])]
    graph = Graph(edges)
    graph.draw()
            

def left_turn(p1, p2, p3):

    #return s1.vector().normalize().angle() < s2.vector().normalize().angle()


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
        raise


def test():
    p1 = Point.null()
    p2 = Point.unit()
    p3 = Point(1, 1, 0)
    p4 = Point(1, -1, 0)

    print(left_turn(p1, p2, p3))
    print(left_turn(p1, p2, p4))
    


def main():

    scale = 10
    points = [Point.random(scale) for e in range(100)]
    [p.draw() for p in points]

    graham_scan(points)

    #test()



if __name__ == "__main__":
    main()
