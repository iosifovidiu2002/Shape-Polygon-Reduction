from sympy import Line

def douglas_peucker(points, epsilon):
    dmax = 0
    index = -1
    end = len(points)
    for i in range(1, end-2):
        d = Line(points[0], points[end-1]).distance(points[i])
        if d > dmax:
            index = i
            dmax = d
    
    if dmax > epsilon:
        left_results = douglas_peucker(points[:index], epsilon)
        right_results = douglas_peucker(points[index:], epsilon)

        result_points = left_results[:len(left_results)-1] + right_results[:len(right_results)]
    else:
        result_points = [points[0], points[end-1]] 
    
    return result_points