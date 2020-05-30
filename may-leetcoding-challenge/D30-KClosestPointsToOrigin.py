# Time Complexity: O(N logN), where N is the length of points.
# Space Complexity: O(N)

def kClosest(points, K):
    points.sort(key= lambda p: p[0]**2 + p[1]**2)
    return points[:K]


print(kClosest([[1,3],[-2,2]], 1))
print(kClosest([[3,3],[5,-1],[-2,4]], 2))