# Same as - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
# Same as - https://leetcode.com/problems/non-overlapping-intervals/

def merge(intervals):
    if not intervals:
        return []
    
    # sort with start
    intervals = sorted(intervals, key=lambda i:i[0])
    
    res = [intervals[0]]
    
    for interval in intervals[1:]:
        if interval[0] <= res[-1][1]:
            res[-1][1] = max(interval[1], res[-1][1])
        else:
            res.append(interval)
            
    return res


print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[4,5]]))
