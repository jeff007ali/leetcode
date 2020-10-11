# Same as - https://leetcode.com/problems/non-overlapping-intervals/
# Same as - https://leetcode.com/problems/merge-intervals/

def findMinArrowShots(points):
    # sort with end
    points = sorted(points, key=lambda p: p[1])
    res = 0
    end = -float('inf')

    for interval in points:
        if interval[0] > end:
            res += 1
            end = interval[1]

    return res


print(findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
print(findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))