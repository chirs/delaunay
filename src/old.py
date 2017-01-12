
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
