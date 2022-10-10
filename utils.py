from sympy import Point
import sys

def save_perimeter_to_file(filename, points):
    lines = []
    for point in points:
        lines.append(f"{point.x} {point.y}")
    with open(filename, 'w') as f:
        f.writelines('\n'.join(lines))

def get_closest(point, points):
    dist_min = float('inf')
    closest = None
    for other in points:
        dist = point.distance(other)
        if dist < dist_min:
            closest = other
            dist_min = dist
    return closest

def rearrange_points(points):
    new_order = []
    point_set = set(points)
    current_point = points[0]
    while len(point_set) > 0:
        closest = get_closest(current_point, point_set)
        new_order.append(current_point)
        current_point = closest
        point_set.remove(current_point)
    return new_order

def read_perimeter_from_file(filename):
    points = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.split()
            points.append(Point(float(line[0]), float(line[1])))

    return points