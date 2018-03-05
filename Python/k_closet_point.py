from math import sqrt

tmp = {}
def distance(point):
    return sqrt(point[0]**2+point[1]**2)

def k_closet(points,k):
    for point in points:
        tmp[float(distance(point))]=point
    return [tmp[i] for i in sorted(tmp.keys())[:k]]

print k_closet([(1,1),(2,2),(3,3),(2,3)],3)
